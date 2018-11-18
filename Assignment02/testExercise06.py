import exercise06
import unittest
import numpy as np
class TestPrimeAndTime(unittest.TestCase):
#    def __init__(self):
 #       obj = exercise05.PrimeCalculator()
    def setUp(self):
        self.testDataAnalyser = exercise06.DataAnalyser(5000)

    #testing that our function return non zeroresult for each of the operation
    #with given non-zero entries
    def test_NonZeroResult(self):
        self.assertNotEqual(self.testDataAnalyser.sum(),0)
        self.assertNotEqual(self.testDataAnalyser.product(),0)
        self.assertNotEqual(self.testDataAnalyser.average(),0)
        self.assertNotEqual(self.testDataAnalyser.variance(),0)
        self.assertNotEqual(self.testDataAnalyser.minimum(),0)
        self.assertNotEqual(self.testDataAnalyser.maximum(),0)

    #testing that our functions return 0 or 1 for empty list as a data
    def test_ZeroEntryorEmptyList(self):
        self.testDataAnalyser = exercise06.DataAnalyser(0)
        self.assertEqual(self.testDataAnalyser.sum(),0)
        self.assertEqual(self.testDataAnalyser.product(),1)

    #testing that our functions return float result for given entries
    def test_TypeofResult(self):
        self.assertEqual(type(self.testDataAnalyser.sum()), float)
        self.assertEqual(type(self.testDataAnalyser.average()), np.float64)
        self.assertEqual(type(self.testDataAnalyser.variance()), np.float64)
        self.assertEqual(type(self.testDataAnalyser.maximum()), float)
        self.assertEqual(type(self.testDataAnalyser.minimum()), float)

    #testing that our functions add properly with normal numpy class having
    # error less than 1e-5
    def test_ResultofFunction(self):
        self.assertTrue(np.abs(np.sum(self.testDataAnalyser.data)-self.testDataAnalyser.sum())<1e-5)
        avg = sum(self.testDataAnalyser.data)/len(self.testDataAnalyser.data)
        self.assertTrue(np.abs(avg-self.testDataAnalyser.average())<1e-5)

    #testing that our list contains random number between 0 to 10000
    def test_RangeofNumber(self):
        self.assertTrue(self.testDataAnalyser.maximum()<10000)


if __name__ == '__main__':
    unittest.main()
