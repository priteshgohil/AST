"""
-------------------------------------------------------------------------------------------------
Developer: Harsh Munshi

Intent: Object list merger. Merging the contents of the list from readings from various sensors

Sensors: RGB, RGBD cameras
-------------------------------------------------------------------------------------------------
"""

"""
Approach:

If the "class" detected by all the sensors (two in this case) is not the same:
	Go with the one with higher probability.
else if classes are the same:
	probabilistic approach

How do we determine the probabilities:
- Check if priors are given. Let's say we have an entry (spoon, 3, 33%)
- Do we know that is p(knife|spoon)?
- We do know that p(others|spoon) = 1-33 = 77%.
- Assuming every object is likely, p(knife) = p(scissor) = p(fork) = p(spoon) = p(keys) = 0.2
- With this assumption, p(object1|object2) = p(object2|object1)
- Now for the same object, the options are 33 and 99
- Which means that there was a 77% chance that it would have been other object.
- Using belief propogation, p(knife) = p(knife|knife,others).p(others|spoon)
- So in this example p(knife) = 0.77*0.99 = 0.7623
- And p(spoon) = 0.01*0.33 = 0.0033
- Adding a normalizer,
  * p(knife) = (1/(0.0033+0.7623))*0.7623 = 0.9956
  * p(spoon) = 1 - 0.9956 = 0.00xx
"""

import os, sys
import configparser
import math
import numpy as np 

class Defaults(object):
	"""A parent class that contains all the resquired defaults """
	def __init__(self, configfile='config.ini', method="average"):
		super(Defaults, self).__init__()
		self.config = configparser.ConfigParser()
		self.file_ = self.config.read(configfile)
		self.method = method
		print("Read config file")

class OLB(Defaults):
	"""docstring for OLB"""
	def __init__(self):
		super(OLB, self).__init__()
		self.merged = []
		self.sensor_readings = {}

		# configurable parameter
		self.num_readings = 4
		self.max_length = 0

	def _merge(self, sensor_data):
		#self.rgb = self.file_['sensors']['RGB']
		#self.rgbd = self.file_['sensors']['RGBD']

		for i in range(self.num_readings):
			self.sensor_readings[i] = {}
			self.sensor_readings[i]["data"] = sorted(sensor_data[i], key=lambda x:x[1])
			self.sensor_readings[i]["length"] = len(self.sensor_readings[i]["data"])
			self.max_length = max(self.sensor_readings[i]["length"], self.max_length)

		# self.max_length is the list of length of the list
		# Fill the entries now

		for key in self.sensor_readings:
				if len(self.merged) == 0:
					self.merged.append(self.sensor_readings[key]["data"])
				else:
					if len(self.sensor_readings[key]["data"]) > len(self.merged[-1]):
						for i in range(len(self.sensor_readings[key]["data"])-len(self.merged[-1])):
							








if __name__ == '__main__':
	red_1 = [('knife',1, 0.55), ('scissor', 2, 0.95), ('fork', 3, 0.99), ('spoon', 4, 0.80), ('keys', 5, 0.95)]
	red_2 = [('knife',1, 0.99), ('scissor', 2, 0.65), ('spoon', 3, 0.33), ('spoon', 4, 0.98), ('keys', 5, 0.50)]
	red_3 = [('knife',1, 0.55), ('scissor', 2, 0.95), ('fork', 3, 0.99), ('spoon', 4, 0.80), ('keys', 5, 0.95)]
	red_4 = [('knife',1, 0.55), ('scissor', 2, 0.95), ('fork', 3, 0.99), ('spoon', 4, 0.80), ('keys', 5, 0.95)]
	merger_object = OLB()
	merger_object._merge([red_1,red_2,red_3,red_4])