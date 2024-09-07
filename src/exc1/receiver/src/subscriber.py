#!/usr/bin/env python

import rospy
from std_msgs.msg import Int32

def callback(data):
    q = 0.15
    outcome= int(data.data * q)
    pub.publish(outcome)

def listner():
    global pub
    rospy.init_node('nodeB', anonymous = True)
    rospy.Subscriber('Gao', Int32, callback)
    pub = rospy.Publisher('kthfs/result', Int32, queue_size = 10)
    rospy.spin()

if __name__ == '__main__':
    listner()