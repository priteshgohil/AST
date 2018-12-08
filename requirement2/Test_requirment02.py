import unittest
import requirement1
import numpy as np

class TestModularity(unittest.TestCase):

    def setUp(self):
        self.Fuseddata = requirement1.FusionOfList()

    #Test total number of object in the final result
    def test_numberof_objects(self):
        rgb_data_algo_1 = [('knife', 1, 99), ('scissor', 2, 95), ('fork', 3, 99)]
        rgb_data_algo_2 = [('knife', 1, 65), ('scissor', 2, 23), ('fork', 3, 48)]
        rgbd_data_algo_1 =  [('knife', 1, 68), ('scissor', 2, 53), ('fork', 3, 46)]
        rgbd_data_algo_2 =  [('knife', 1, 86), ('scissor', 2, 27), ('fork', 3, 84)]
        dummy = ['z', 'z', 'z']
        Final_Data = np.vstack((rgb_data_algo_1,dummy,rgb_data_algo_2,dummy,rgbd_data_algo_1,dummy,rgbd_data_algo_2))
        combi_data = self.Fuseddata.get_most_confident_data(Final_Data)
        self.assertEqual(len(combi_data),3)
        rgb_data_algo_1 = [('knife', 1, 81), ('scissor', 2, 35), ('fork', 3, 88),('spoon', 4, 34)]
        rgb_data_algo_2 = [('knife', 1, 65), ('scissor', 2, 68), ('fork', 3, 75),('spoon', 4, 68)]
        rgbd_data_algo_1 =  [('knife', 1, 95), ('scissor', 2, 81), ('fork', 3, 58),('spoon', 4, 84)]
        rgbd_data_algo_2 =  [('knife', 1, 32), ('scissor', 2, 84), ('fork', 3, 65),('spoon', 4, 79)]
        Final_Data = np.vstack((rgb_data_algo_1,dummy,rgb_data_algo_2,dummy,rgbd_data_algo_1,dummy,rgbd_data_algo_2))
        combi_data = self.Fuseddata.get_most_confident_data(Final_Data)
        self.assertEqual(len(combi_data),4)


    #Test tag associated with each input
    def test_inputs_tag_match(self):
        rgb_data = np.array([('knife', 1, 99), ('scissor', 2, 95), ('fork', 3, 99),('spoon', 4, 98)])
        for object_data in rgb_data:
            if object_data[0] == 'knife':
                self.assertEqual(object_data[1],1)
            elif object_data[0] == 'scissor':
                self.assertEqual(object_data[1],2)
            elif object_data[0] == 'fork':
                self.assertEqual(object_data[1],3)
            elif object_data[0] == 'spoon':
                self.assertEqual(object_data[1],4)
        rgbd_data =  [('knife', 1, 88), ('scissor', 2, 53), ('fork', 4, 66),('spoon', 3, 63)]
        for object_data in rgbd_data:
            if object_data[0] == 'knife':
                self.assertEqual(object_data[1],1)
            elif object_data[0] == 'scissor':
                self.assertEqual(object_data[1],2)
            elif object_data[0] == 'fork':
                self.assertEqual(object_data[1],3)
            elif object_data[0] == 'spoon':
                self.assertEqual(object_data[1],4)

    #test the values in porbability are in range of 0 to 100
    def test_probability_in_limits(self):
        rgb_data_algo_1 = [('knife', 1, 95), ('scissor', 2, 81), ('fork', 3, 58),('spoon', 4, 84)]
        rgb_data_algo_2 = [('knife', 1, 65), ('scissor', 2, 68), ('fork', 3, 75),('spoon', 4, 68)]
        rgbd_data_algo_1 =  [('knife', 1, 81), ('scissor', 2, 35), ('fork', 3, 88),('spoon', 4, 34)]
        rgbd_data_algo_2 =  [('knife', 1, 32), ('scissor', 2, 84), ('fork', 3, 65),('spoon', 4, 79)]
        combi_data = self.Fuseddata.get_most_confident_data((rgb_data_algo_1,dummy,rgb_data_algo_2,dummy,rgbd_data_algo_1,dummy,rgbd_data_algo_2))
        for object_data in combi_data:
            self.assertTrue(object_data[2] >= 0.0 and object_data[2] <= 100.0)

    #test the values in porbability are not in range of 0 to 100
    def test_probability_notin_limits(self):
        rgbd_data_algo_2 =  [('knife', 1, 88), ('scissor', 2, 123), ('fork', 3, 66),('spoon', 4, =35)]
        rgb_data_algo_1 = [('knife', 1, 99), ('scissor', 2, 95), ('fork', 3, 99),('spoon', 4, 98)]
        rgb_data_algo_2 = [('knife', 1, 65), ('scissor', 2, 68), ('fork', 3, 75),('spoon', 4, 68)]
        rgbd_data_algo_1 =  [('knife', 1, 81), ('scissor', 2, 35), ('fork', 3, 88),('spoon', 4, 34)]
        combi_data = self.Fuseddata.get_most_confident_data((rgb_data_algo_1,dummy,rgb_data_algo_2,dummy,rgbd_data_algo_1,dummy,rgbd_data_algo_2))
        for object_data in combi_data:
            if object_data[2] >100 and object_data[2] <0:
                self.assertTrue(True)

    #Test for output format as given in input
    def test_outputs_format(self):
        rgb_data_algo_1 = [('knife', 1, 99), ('scissor', 2, 95), ('fork', 3, 99),('spoon', 4, 69)]
        rgbd_data_algo_1 =  [('knife', 1, 88), ('scissor', 2, 65), ('fork', 3, 66),('spoon', 4,85)]
        rgb_data_algo_2 = [('knife', 1, 65), ('scissor', 2, 68), ('fork', 3, 75),('spoon', 4, 68)]
        rgbd_data_algo_2 =  [('knife', 1, 81), ('scissor', 2, 35), ('fork', 3, 88),('spoon', 4, 34)]
        combi_data = self.Fuseddata.get_most_confident_data((rgb_data_algo_1,dummy,rgb_data_algo_2,dummy,rgbd_data_algo_1,dummy,rgbd_data_algo_2))
        self.assertEqual(combi_data,[('knife', 1, 99),('scissor', 2, 95),('fork', 3, 99),('spoon', 4,85)])

    #if size of two input list doesnt match throw an error.
    def test_mismatched_list(self):
        rgb_data_algo_ = [('knife', 1, 99), ('scissor', 2, 95), ('fork', 3, 99)]
        rgbd_data =  [('knife', 1, 88), ('scissor', 2, 65), ('fork', 3, 66),('spoon', 4,85)]
        rgbd_data_algo_2 =  [('knife', 1, 65), ('scissor', 2, 68), ('fork', 3, 75),('spoon', 4, 68)]
        rgb_data_algo_2 = [('scissor', 2, 95), ('fork', 3, 99),('knife', 1, 99)]
        combi_data = self.Fuseddata.get_most_confident_data((rgb_data_algo_1,dummy,rgb_data_algo_2,dummy,rgbd_data_algo_1,dummy,rgbd_data_algo_2))
        self.assertEqual(combi_data,[('knife', 1, 99),('scissor', 2, 95),('fork', 3, 99),('spoon', 4,85)])

    def test_unsorted_list(self):
        rgb_data = [ ('scissor', 2, 95), ('fork', 3, 99),('knife', 1, 34)]
        rgbd_data =  [('knife', 1, 88), ('spoon', 4,85), ('scissor', 2, 65), ('fork', 3, 66)]
        rgbd_data_algo_2 =  [('knife', 1, 65), ('scissor', 2, 68), ('fork', 3, 75),('spoon', 4, 68)]
        rgb_data_algo_2 = [('knife', 1, 81), ('scissor', 2, 35), ('fork', 3, 88),('spoon', 4, 99)]
        combi_data = self.Fuseddata.get_most_confident_data((rgb_data_algo_1,dummy,rgb_data_algo_2,dummy,rgbd_data_algo_1,dummy,rgbd_data_algo_2))
        self.assertEqual(combi_data,[('knife', 1, 88),('scissor', 2, 95),('fork', 3, 88),('spoon', 4,99)])


if __name__ == '__main__':
    unittest.main()
