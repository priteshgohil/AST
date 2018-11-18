import exercise05
import unittest

class TestPrimeAndTime(unittest.TestCase):
#    def __init__(self):
 #       obj = exercise05.PrimeCalculator()
    def setUp(self):
        self.prime = exercise05.PrimeCalculator()
        self.time = exercise05.TimeMeasurer()
    def test_Prime_number(self):
        data = self.prime.calculate(115)
        self.assertEqual(data[2],5)
        self.assertGreater(115, len(data))
        self.assertNotIn(115, data)
        self.assertNotEqual(data,[])
    def test_TimeTaken(self):
        MAX_INT = 100000
        self.time.start()
        self.prime.calculate(MAX_INT)
        self.time.stop()
        timeTaken = self.time.get()
        self.assertLess(timeTaken, 0.1)

        self.time.start()
        self.prime.calculate(MAX_INT*10)
        self.time.stop()
        self.assertLess(self.time.get(), 0.1*10)

    def test_TimeModule(self):
        self.time.start()
        no_op = 0
        self.time.stop()
        self.assertNotEqual(self.time.get(),0.0)


if __name__ == '__main__':
    unittest.main()
