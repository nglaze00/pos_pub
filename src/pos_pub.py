#!/usr/bin/env python  
import roslib
import rospy
import math
import tf
import geometry_msgs.msg
f = open('xy.txt', 'w')
if __name__ == '__main__':
    rospy.init_node('pos_pub')

    listener = tf.TransformListener()

    rate = rospy.Rate(10.0)
    while not rospy.is_shutdown():
        try:
            (trans,rot) = listener.lookupTransform('/map', '/base_link', rospy.Time(0))
        except (tf.LookupException, tf.ConnectivityException, tf.ExtrapolationException):
            continue

        print("x: ",str(trans[0]))
        print("y: ",str(trans[1]))
        f.write(str(trans[0]) + "," + str(trans[1]) + "\n")
        
        rate.sleep()

f.close()


       
