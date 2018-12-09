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
		self.max_length = 5

	def _merge(self, sensor_data):
		#self.rgb = self.file_['sensors']['RGB']
		#self.rgbd = self.file_['sensors']['RGBD']

		for i in range(self.num_readings):
			self.sensor_readings[i] = {}
			self.sensor_readings[i]["data"] = sorted(sensor_data[i], key=lambda x:x[1])
			self.sensor_readings[i]["length"] = len(self.sensor_readings[i]["data"])

        if self.method == "average":
        	_new_list = self._average(self.sensor_readings)

        else:
			for key in self.sensor_readings:
				if self.sensor_readings[key]["length"] < self.max_length:
					pass
				else:
					if len(self.merged) == 0:
						self.merged.append(self.sensor_readings[key]["data"])
					else:
						_new_list = self._data_fusion(self.merged[-1], self.sensor_readings[key]["data"])
						self.merged = []
						self.merged.append(_new_list)

		print(_new_list)


	def _data_fusion(self, data_1, data_2):
		self.merged_local = []
		for rgb_data, rgbd_data in zip(data_1, data_2):
			if rgb_data[0] == rgbd_data[0]:
				self.merged_local.append((rgb_data[0], rgb_data[1], np.mean([rgb_data[2],rgbd_data[2]])))
			else:
				if rgb_data[2] > rgbd_data[2]:
					_probability_others = 1 - rgbd_data[2]
					_probaility_net_other_class = rgb_data[2]*_probability_others
					_probaility_net_same_class = (1-rgb_data[2])*rgbd_data[2]
					normalizer = 1/(_probaility_net_other_class+_probaility_net_same_class)
					self.merged_local.append((rgb_data[0],rgb_data[1], normalizer*_probaility_net_other_class))
				else:
					_probability_others = 1 - rgb_data[2]
					_probaility_net_other_class = rgbd_data[2]*_probability_others
					_probaility_net_same_class = (1-rgbd_data[2])*rgb_data[2]
					normalizer = 1/(_probaility_net_other_class+_probaility_net_same_class)
					self.merged_local.append((rgbd_data[0],rgbd_data[1], normalizer*_probaility_net_other_class))
		return self.merged_local

	def _normal(self, sensor_data):
		for list1,list2, list3, list4 in zip(sensor_data[0], sensor_data[1], sensor_data[2], sensor_data[3]):
			max_arg = np.argmax(list1[2],list2[2],list3[2],list4[2])








if __name__ == '__main__':
	red_1 = [('knife',1, 0.55), ('scissor', 2, 0.95), ('fork', 3, 0.99), ('spoon', 4, 0.80), ('keys', 5, 0.95)]
	red_2 = [('knife',1, 0.99), ('scissor', 2, 0.65), ('spoon', 3, 0.33), ('spoon', 4, 0.98), ('keys', 5, 0.50)]
	red_3 = [('knife',1, 0.55), ('scissor', 2, 0.95), ('fork', 3, 0.99), ('spoon', 4, 0.80), ('keys', 5, 0.95)]
	red_4 = [('knife',1, 0.55), ('scissor', 2, 0.95), ('fork', 3, 0.99), ('spoon', 4, 0.80), ('keys', 5, 0.95)]
	merger_object = OLB()
	merger_object._merge([red_1,red_2,red_3,red_4])