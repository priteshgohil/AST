import unittest
import exercise07

class TestFunCalc(unittest.TestCase):

    def setUp(self):
        self.object_calc = exercise07.FunctionCalculator()

    #checking value with k and n having difference of 100 value
    def test_FunctionValueForRange0to200(self):
        Val = self.object_calc.calculate(100,200)
        Val_expec = float(1.0/730.0)
        self.assertTrue((Val - Val_expec) < 1e-5)

    # checking value with k and n with 4 values
    def test_FunctionValueForRange0to10(self):
        Val = self.object_calc.calculate(6,10)
        Val_expec = float(1.0/9.0)
        self.assertTrue((Val - Val_expec) <= 1e-1)

    #testing value of function for k and n having difference is only 1
    def test_FunctionValueForRange0to801(self):
        Val = self.object_calc.calculate(800,801)
        Val_expec = float(1.1123)
        self.assertTrue((Val - Val_expec) <= 1e-1)

    #testing for Zero input for range
    def test_FunctionValueForZeroInput(self):
        Val = self.object_calc.calculate(0,0)
        self.assertEqual(Val, 0.0)

    #testing for 1 input for range
    def test_FunctionValueForOneNumber(self):
        Val = self.object_calc.calculate(0,1)
        self.assertEqual(Val, 0.5)

if __name__=='__main__':
    unittest.main()

