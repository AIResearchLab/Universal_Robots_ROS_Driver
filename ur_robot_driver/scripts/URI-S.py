#!/usr/bin/env python
import rospy
import time
from control_msgs.msg import JointTrajectoryControllerState

def callback(data):
     rospy.loginfo(data)
     
def listener():

    rospy.init_node('uris', anonymous=True)
    rospy.Subscriber("arm_controller/state", JointTrajectoryControllerState, callback)
    rospy.spin()
if __name__ == '__main__':
    listener()