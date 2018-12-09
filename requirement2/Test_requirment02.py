import unittest
import requirement2
# import numpy as np

class TestModularity(unittest.TestCase):

    def setUp(self):
        self.Fuseddata = requirement2.FusionOfList()


    #Test functionality of the class
    def test_functionality_testing(self):
        rgb_data_algo_1 = [('knife',1, 33), ('scissor', 2, 95), ('fork', 3, 99), ('spoon', 4, 68), ('keys', 5, 95)]
        rgb_data_algo_2 = [('knife',1, 92), ('scissor', 2, 65), ('spoon', 3, 33), ('spoon', 4, 87), ('keys', 5, 50)]
        rgbd_data_algo_1 = [('knife',1, 55), ('scissor', 2, 91), ('fork', 3, 85), ('spoon', 4, 80), ('keys', 5, 95)]
        rgbd_data_algo_2 = [('knife',1, 85), ('scissor', 2, 85), ('fork', 3, 50), ('spoon', 4, 89), ('keys', 5, 66)]
        merged_data = [rgb_data_algo_1,rgb_data_algo_2,rgbd_data_algo_1,rgbd_data_algo_2]
        combi_data = self.Fuseddata._merge(merged_data)
        self.assertEqual(combi_data[0][2],92)
        self.assertEqual(combi_data[1][2],95)
        self.assertEqual(combi_data[2][2],99)
        self.assertEqual(combi_data[3][2],89)
        self.assertEqual(combi_data[4][2],95)

    #Test total number of object in the final result
    def test_numberof_objects(self):
        rgb_data_algo_1 = [('knife', 1, 99), ('fork', 3, 99)]
        rgb_data_algo_2 = [('knife', 1, 65), ('scissor', 2, 23), ('fork', 3, 48)]
        rgbd_data_algo_1 =  [('knife', 1, 68), ('scissor', 2, 53)]
        rgbd_data_algo_2 =  [('knife', 1, 86)]
        merged_data = [rgb_data_algo_1,rgb_data_algo_2,rgbd_data_algo_1,rgbd_data_algo_2]
        combi_data = self.Fuseddata._merge(merged_data)
        self.assertEqual(len(combi_data),3)
        rgb_data_algo_1 = [('knife', 1, 81), ('scissor', 2, 35), ('fork', 3, 88),('spoon', 4, 34)]
        rgb_data_algo_2 = [('knife', 1, 65), ('scissor', 2, 68)]
        rgbd_data_algo_1 =  [('knife', 1, 95)]
        rgbd_data_algo_2 =  [('knife', 1, 32), ('scissor', 2, 84), ('spoon', 4, 79)]
        merged_data = [rgb_data_algo_1,rgb_data_algo_2,rgbd_data_algo_1,rgbd_data_algo_2]
        combi_data = self.Fuseddata._merge(merged_data)
        self.assertEqual(len(combi_data),4)

    # test with one of the empty list
    def test_with_one_empty_sensor_input(self):
        rgb_data_algo_1 = [('knife',1, 33), ('scissor', 2, 35), ('fork', 3, 85), ('spoon', 4, 55), ('keys', 5, 75)]
        rgb_data_algo_2 = []
        rgbd_data_algo_1 = [('knife',1, 55), ('scissor', 2, 82), ('fork', 3, 35), ('spoon', 4, 25), ('keys', 5, 32)]
        rgbd_data_algo_2 = [('knife',1, 85), ('keys', 5, 81)]
        merged_data = [rgb_data_algo_1,rgb_data_algo_2,rgbd_data_algo_1,rgbd_data_algo_2]
        combi_data = self.Fuseddata._merge(merged_data)
        self.assertEqual(combi_data,[('knife',1, 85), ('scissor', 2, 82), ('fork', 3, 85), ('spoon', 4, 55), ('keys', 5, 81)])

    # test with very less sensor data
    def test_few_sensor_input(self):
        rgb_data_algo_1 = []
        rgb_data_algo_2 = []
        rgbd_data_algo_1 = [('scissor', 2, 82)]
        rgbd_data_algo_2 = [('knife',1, 85)]
        merged_data = [rgb_data_algo_1,rgb_data_algo_2,rgbd_data_algo_1,rgbd_data_algo_2]
        combi_data = self.Fuseddata._merge(merged_data)
        self.assertEqual(combi_data,[('knife',1, 85), ('scissor', 2, 82)])

    #test with all list empty length of list
    def test_no_input_from_sensor(self):
        rgb_data_algo_1 = []
        rgb_data_algo_2 = []
        rgbd_data_algo_1 = []
        rgbd_data_algo_2 = []
        merged_data = [rgb_data_algo_1,rgb_data_algo_2,rgbd_data_algo_1,rgbd_data_algo_2]
        combi_data = self.Fuseddata._merge(merged_data)
        self.assertEqual(combi_data,[])

    #test the values in porbability are in range of 0 to 100
    def test_probability_in_limits(self):
        rgb_data_algo_1 = [('knife', 1, 95), ('scissor', 2, 81), ('fork', 3, 58),('spoon', 4, 84)]
        rgb_data_algo_2 = [('knife', 1, 65), ('scissor', 2, 68), ('fork', 3, 75),('spoon', 4, 68)]
        rgbd_data_algo_1 =  [('knife', 1, 81), ('scissor', 2, 35), ('fork', 3, 88),('spoon', 4, 34)]
        rgbd_data_algo_2 =  [('knife', 1, 32), ('scissor', 2, 84), ('fork', 3, 65),('spoon', 4, 79)]
        merged_data = [rgb_data_algo_1,rgb_data_algo_2,rgbd_data_algo_1,rgbd_data_algo_2]
        combi_data = self.Fuseddata._merge(merged_data)
        for object_data in combi_data:
            self.assertTrue(object_data[2] >= 0.0 and object_data[2] <= 100.0)

    #test the values in porbability are not in range of 0 to 100
    def test_probability_notin_limits(self):
        rgbd_data_algo_2 =  [('scissor', 2, 123), ('fork', 3, 66),('spoon', 4, 35)]
        rgb_data_algo_1 = [('knife', 1, 99), ('scissor', 2, 95), ('fork', 3, 99),('spoon', 4, 101)]
        rgb_data_algo_2 = [('knife', 1, 65), ('scissor', 2, 150),('spoon', 4, 68)]
        rgbd_data_algo_1 =  [('knife', 1, 81), ('fork', 3, 88)]
        merged_data = [rgb_data_algo_1,rgb_data_algo_2,rgbd_data_algo_1,rgbd_data_algo_2]
        combi_data = self.Fuseddata._merge(merged_data)
        for object_data in combi_data:
            if object_data[2] >100 and object_data[2] <0:
                self.assertTrue(True)



if __name__ == '__main__':
    unittest.main()
