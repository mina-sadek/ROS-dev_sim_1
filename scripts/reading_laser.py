#! /usr/bin/env python

import rospy
from sensor_msgs.msg import LaserScan

def laser_cb(msg):
	# 720/5 = 144
	regions = [
#	min(msg.ranges[0:15]),
#	720/5 = 144
	min(min(msg.ranges[0:143]), 10),
	min(min(msg.ranges[144:287]), 10),
	min(min(msg.ranges[288:431]), 10),
	min(min(msg.ranges[432:575]), 10),
	min(min(msg.ranges[576:713]), 10),
	]
	rospy.loginfo(regions)

def main():
	rospy.init_node('reading_laser')
	sub= rospy.Subscriber("/diff_bot/laser/scan", LaserScan, laser_cb)

	rospy.spin()

if __name__ == '__main__':
	main()
