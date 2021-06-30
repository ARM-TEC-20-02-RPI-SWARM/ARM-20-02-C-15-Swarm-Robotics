#!/usr/bin/env python3

import rospy
from std_msgs.msg import Bool
import serial
import time


class arduinoread:
	def __init__(self):
		rospy.init_node('arduino_talker', anonymous=True)
		self.arduino_deadman_switch_topic=rospy.get_param('~arduino_deadman_switch_topic')
		self.arduino_e_stop_topic=rospy.get_param('~arduino_e_stop_topic')
		
		self.comport=rospy.get_param('~com_port')
		
		self.ser = serial.Serial(self.comport,115200,timeout=0.04)
		
		self.deadman_switch_pub = rospy.Publisher(self.arduino_deadman_switch_topic, Bool, queue_size=1)
		self.e_stop_pub = rospy.Publisher(self.arduino_e_stop_topic, Bool, queue_size=1)
		time.sleep(1)
		rospy.Timer(rospy.Duration(0.04),self.read_serial)


	def read_serial(self,event):
		if not rospy.is_shutdown():
			output=int(self.ser.read())
			mes_deadman_switch = Bool()
			mes_e_stop = Bool()

			if(output == 0):
				mes_e_stop.data = 0
				mes_deadman_switch.data = 0
			if(output == 1):
				mes_e_stop.data = 0
				mes_deadman_switch.data = 1
			if(output == 2):
				mes_e_stop.data = 1
				mes_deadman_switch.data = 0
			if(output == 3):
				mes_e_stop.data = 1
				mes_deadman_switch.data = 0


			self.deadman_switch_pub.publish(mes_deadman_switch)
			self.e_stop_pub.publish(mes_e_stop)

			self.ser.reset_input_buffer()
		else:
			rospy.signal_shutdown("system shutdown")








if __name__ == '__main__':
	arduinoreader=arduinoread()

	# Subscribe to space mouse velocity commands
	
	# Publish command velocity
	

	rospy.spin()