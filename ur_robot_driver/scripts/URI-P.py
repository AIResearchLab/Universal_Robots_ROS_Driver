#!/usr/bin/env python
import rospy
import time
import numpy
from std_msgs.msg import Float64MultiArray

def home():
    executeck = raw_input("Execute Current Waypoints? (y/n): ")
    if executeck == "y":
        talker()
    else:
        waypointck = raw_input("Add Waypoints? (y/n): ")
        if waypointck == "y":
            print("Not Supported on Sim")
            home()
        else:
            exit()

def talker():
    pub = rospy.Publisher('/joint_group_position_controller/command', Float64MultiArray, queue_size=10)
    rospy.init_node('urcom', anonymous=True)
    rate = rospy.Rate(50)
    homepos = Float64MultiArray(data=[0.00, 0.00, 0.00, 0.00, 0.00, 0.00])
    pub.publish(homepos)
    addway = [[0.00, -1.00, 1.00, 1.00, 1.57, 1.00],[0.00, -1.00, 1.00, 0.00, 3.14, 0.00],[0.00, 0.00, 0.00, 0.00, 0.00, 0.00]]
    Waypoints = []
    Waypoints = Waypoints+addway
    print("Available Waypoints: ", Waypoints)
    wpn = len(Waypoints)
    wpc = 0
    while not rospy.is_shutdown():
        Pos = Float64MultiArray()
        while wpc < wpn:
            print("Executing Waypoint: ", wpc)
            Pos.data = Waypoints[wpc]
            pub.publish(Pos)
            time.sleep(1.5)
            print("Reached Waypoint: ", wpc)
            wpc = wpc+1
            if(wpc == (wpn)):
                home()
if __name__ == '__main__':
    home()