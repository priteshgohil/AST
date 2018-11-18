import sys
import time
import numpy as np

MAX_INT = 2147483647

class PrimeCalculator:
    def __init__(self):
        pass

    def calculate(self, n):
        r = []
        l = np.ones(n, bool)
        #l = [True] * n
        l[0] = l[1] = False
        for i, b in enumerate(l):
            if b:
                r.append(i)
                for n in np.arange(i * i, n, i):
                    l[n] = False
        return r

class TimeMeasurer:
    def __init__(self):
        self.time = 0

    def start(self):
        self.time = time.time()
    
    def stop(self):
        self.time = time.time() - self.time

    def get(self):
        return self.time

prime_calculator = PrimeCalculator()
time_measurer = TimeMeasurer()
time_measurer.start()
prime_calculator.calculate(MAX_INT / 1000)
time_measurer.stop()
print("Time: ", time_measurer.get())
