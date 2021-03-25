#!/usr/bin/env python
import rospy
import time
import numpy
from sensor_msgs.msg import JointState

def callback(data):
     print(numpy.around(data.position,3))
     
def listener():

    rospy.init_node('uris', anonymous=True)
    rospy.Subscriber("joint_states", JointState, callback)
    rospy.spin()
if __name__ == '__main__':
    listener()