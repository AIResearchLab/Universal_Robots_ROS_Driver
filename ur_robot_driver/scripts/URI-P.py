#!/usr/bin/env python
import rospy
import time
import numpy
from std_msgs.msg import Float64MultiArray

def talker():
    pub = rospy.Publisher('/joint_group_position_controller/command', Float64MultiArray, queue_size=10)
    rospy.init_node('urcom', anonymous=True)
    rate = rospy.Rate(50)
    Waypoints1 = [0.00, 0.00, 0.00, 0.00, 0.00, 0.00]
    Waypoints2 = [0.00, -1.00, 1.00, 0.00, 1.57, 0.00]
    while not rospy.is_shutdown():
        Pos1 = Float64MultiArray()
        Pos1.data = Waypoints1
        Pos2 = Float64MultiArray()
        Pos2.data = Waypoints2
        #check if user wants to add another waypoint to the sequence
        executeck = raw_input("Execute Current Waypoints? (y/n): ")
        if executeck == "y":
            pub.publish(Pos1)
            time.sleep(4)
            pub.publish(Pos2)
            time.sleep(4)
        else:
            rate.sleep()
        
if __name__ == '__main__':
    talker()