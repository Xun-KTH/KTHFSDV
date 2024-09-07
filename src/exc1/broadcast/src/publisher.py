#!/usr/bin/env python

import rospy
from std_msgs.msg import Int32

def publisher():
    pub = rospy.Publisher('Gao', Int32, queue_size=10)
    rospy.init_node('nodeA', anonymous=True)
    rate = rospy.Rate(20)
    k = 1
    n = 4
    while not rospy.is_shutdown():
        pub.publish(k)
        k += n
        rate.sleep()

if __name__ == '__main__':
    try:
        publisher()
    except rospy.ROSInterruptException:
        pass