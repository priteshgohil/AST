"""
-------------------------------------------------------------------------------------------------
Developer: Harsh Munshi and Pritesh Gohil

Intent: Object list merger. Merging the contents of the list from readings from various sensors

Sensors: RGB, RGBD cameras

Input: List of List of tuple contains Sensors data

Output: List of tuple contains best sensor data
-------------------------------------------------------------------------------------------------
"""

"""
Approach:

Merging all the sensor data list into one and passing it to class.
Class will return only one list containing the objects with highest probability

Operations performed inside class:
- seperate the fused list of tuple and create a dictionary
- check for the each element in each sensor data
- compare with perviously stored best object and if current object has higher
probability then replace it.
- arrange the result into list and return it.
"""

import os, sys
import configparser
import math
import numpy as np

class Defaults(object):
    """A parent class that contains all the resquired defaults """
    def __init__(self, configfile='config.ini'):
        super(Defaults, self).__init__()
        self.config = configparser.ConfigParser()
        self.file_ = self.config.read(configfile)
        print("Read config file")

class FusionOfList(Defaults):
    """docstring for FusionOfList"""
    def __init__(self):
        super(FusionOfList, self).__init__()
        self.merged = []
        self.sensor_readings = {}
        # configurable parameter
        self.max_length = 5

    def _merge(self, sensor_data):
        #self.rgb = self.file_['sensors']['RGB']
        #self.rgbd = self.file_['sensors']['RGBD']
        self.result = []
        self.sensor_data= sensor_data
        self.num_readings = len(self.sensor_data)
        self.best_objects = [0]*self.max_length
        for i in range(self.num_readings):
            self.sensor_readings[i] = {}
            self.sensor_readings[i]["data"] = sorted(sensor_data[i], key=lambda x:x[1])
            self.sensor_readings[i]["length"] = len(self.sensor_readings[i]["data"])

        for key in self.sensor_readings:
            for index in range(self.sensor_readings[key]["length"]):
                # working list by list of sensor data to find best object
                data = (self.sensor_readings[key]["data"][index])
                data_id = data[1]-1
                data_prediction = data[2]
                if self.best_objects[data_id]==0:
                    self.best_objects[data_id] = data
                elif self.best_objects[data_id][2]<data_prediction:
                    self.best_objects[data_id] = data

        if self.best_objects:
            for size in range(len(self.best_objects)):
                temp = self.best_objects.pop(0)
                if temp:
                    self.result.append(temp)
        else:
            self.result = []
        return self.result

if __name__ == '__main__':
    '''#test case 1
    red_1 = [('knife',1, 33), ('scissor', 2, 95), ('fork', 3, 99), ('spoon', 4, 80), ('keys', 5, 95)]
    red_2 = [('knife',1, 92), ('scissor', 2, 65), ('spoon', 3, 33), ('spoon', 4, 98), ('keys', 5, 50)]
    red_3 = [('knife',1, 55), ('scissor', 2, 95), ('fork', 3, 99), ('spoon', 4, 80), ('keys', 5, 95)]
    red_4 = [('knife',1, 85), ('scissor', 2, 95), ('fork', 3, 99), ('spoon', 4, 80), ('keys', 5, 95)]'''

    '''#test case 2 :testing uneven length of list
    red_1 = [('knife',1, 33), ('scissor', 2, 35), ('fork', 3, 85), ('spoon', 4, 55), ('keys', 5, 75)]
    red_2 = [('knife',1, 92), ('spoon', 3, 33), ('spoon', 4, 5), ('keys', 5, 50)]
    red_3 = [('knife',1, 55), ('scissor', 2, 82), ('fork', 3, 35), ('spoon', 4, 25), ('keys', 5, 32)]
    red_4 = [('knife',1, 85), ('keys', 5, 81)]'''

    '''#test case 3 :testing with one of the empty list
    red_1 = [('knife',1, 33), ('scissor', 2, 35), ('fork', 3, 85), ('spoon', 4, 55), ('keys', 5, 75)]
    red_2 = []
    red_3 = [('knife',1, 55), ('scissor', 2, 82), ('fork', 3, 35), ('spoon', 4, 25), ('keys', 5, 32)]
    red_4 = [('knife',1, 85), ('keys', 5, 81)]'''

    #test case 4 :testing with very less sensor data
    red_1 = []
    red_2 = []
    red_3 = [('scissor', 2, 82)]
    red_4 = [('knife',1, 85)]

    '''#test case 5 :testing with all list empty length of list
    red_1 = []
    red_2 = []
    red_3 = []
    red_4 = []'''

    '''#test case 6 :testing with probability limit in range
    red_1 = [('knife',1, 33), ('scissor', 2, 35), ('fork', 3, 85), ('spoon', 4, 55), ('keys', 5, 75)]
    red_2 = []
    red_3 = [('knife',1, 55), ('scissor', 2, 82), ('fork', 3, 105), ('spoon', 4, 25), ('keys', 5, 32)]
    red_4 = [('knife',1, 85), ('keys', 5, 81)]'''

    merger_object = FusionOfList()
    merged_data = [red_1,red_2,red_3,red_4]
    result = merger_object._merge(merged_data)
    print result
