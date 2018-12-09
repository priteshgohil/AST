import unittest
import requirement1

class TestModularity(unittest.TestCase):

    def setUp(self):
        self.Fuseddata = requirement1.FusionOfList()

    #Test total number of object in the final result
    def test_numberof_objects(self):
        rgb_data = [('knife', 1, 99), ('scissor', 2, 95), ('fork', 3, 99)]
        rgbd_data =  [('knife', 1, 88), ('scissor', 2, 53), ('fork', 3, 66)]
        combi_data = self.Fuseddata.get_most_confident_data(rgb_data,rgbd_data)
        self.assertEqual(len(combi_data),3)
        rgb_data = [('knife', 1, 99), ('scissor', 2, 95), ('fork', 3, 99),('spoon', 4, 98)]
        rgbd_data =  [('knife', 1, 88), ('scissor', 2, 53), ('fork', 3, 66),('spoon', 4, 63)]
        combi_data = self.Fuseddata.get_most_confident_data(rgb_data,rgbd_data)
        self.assertEqual(len(combi_data),4)

    #Test tag associated with each input
    def test_inputs_tag_match(self):
        rgb_data = [('knife', 1, 99), ('scissor', 2, 95), ('fork', 3, 99),('spoon', 4, 98)]
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
        rgb_data = [('knife', 1, 99), ('scissor', 2, 95), ('fork', 3, 99),('spoon', 4, 98)]
        rgbd_data =  [('knife', 1, 88), ('scissor', 2, 23), ('fork', 3, 66),('spoon', 4, 35)]
        for object_data in rgb_data:
            self.assertTrue(object_data[2] >= 0.0 and object_data[2] <= 100.0)
        for object_data in rgbd_data:
            self.assertTrue(object_data[2] >= 0.0 and object_data[2] <= 100.0)

    #test the values in porbability are not in range of 0 to 100
    def test_probability_notin_limits(self):
        rgbd_data =  [('knife', 1, 88), ('scissor', 2, 123), ('fork', 3, 66),('spoon', 4, -35)]
        rgb_data = [('knife', 1, 99), ('scissor', 2, 95), ('fork', 3, 99),('spoon', 4, 98)]
        for object_data in rgbd_data:
            if object_data[2] >100 and object_data[2] <0:
                self.assertTrue(True)
        for object_data in rgb_data:
            if object_data[2] >100 and object_data[2] <0:
                self.assertTrue(True)

    #Test for output format as given in input
    def test_outputs_format(self):
        rgb_data = [('knife', 1, 99), ('scissor', 2, 95), ('fork', 3, 99),('spoon', 4, 69)]
        rgbd_data =  [('knife', 1, 88), ('scissor', 2, 65), ('fork', 3, 66),('spoon', 4,85)]
        combi_data = self.Fuseddata.get_most_confident_data(rgb_data,rgbd_data)
        self.assertEqual(combi_data,[('knife', 1, 99),('scissor', 2, 95),('fork', 3, 99),('spoon', 4,85)])

    #if size of two input list doesnt match throw an error.
    def test_mismatched_list(self):
        rgb_data = [('knife', 1, 99), ('scissor', 2, 95), ('fork', 3, 99)]
        rgbd_data =  [('knife', 1, 88), ('scissor', 2, 65), ('fork', 3, 66),('spoon', 4,85)]
        combi_data = self.Fuseddata.get_most_confident_data(rgb_data,rgbd_data)
        self.assertEqual(combi_data,[])

if __name__ == '__main__':
    unittest.main()
