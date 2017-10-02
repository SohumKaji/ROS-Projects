#!/usr/bin/env python  
import rospy

from std_msgs.msg import Int16
from project1_solution.msg import TwoInts

def publish(sums):
	
 	pub = rospy.Publisher('sum', Int16, queue_size=10)
	pub.publish(sums)
	print sums

def callback(data):
 	print data.a, "+", data.b, "="
  	publish(data.a+data.b)

def subscribe():
	rospy.init_node('listener', anonymous=True) 
	rospy.Subscriber("two_ints", TwoInts, callback)
   	rospy.spin()


if __name__ == '__main__':
 
 
 
	subscribe()