#!/usr/bin/env python
import rospy
import time
from sensor_msgs.msg import JointState

def callback(data):
     rospy.loginfo(data)
     
def listener():

    rospy.init_node('uris', anonymous=True)
    rospy.Subscriber("joint_states", JointState, callback)
    rospy.spin()
if __name__ == '__main__':
    listener()