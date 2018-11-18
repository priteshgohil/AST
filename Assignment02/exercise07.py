import numpy as np

class FunctionCalculator:
    def __init__(self):
        pass

    def calculate(self, k, n):
        r = 1
        result = 0
        for i in range(1, n + 1):
            v = 0
            if i == 1:
                v = .5
            elif i > 1 and i < k:
                v = .9
            elif k <= i:
                v = .1
            r *= v / (1 - v)
            result = (float)(1.0 - (1.0 + r) ** -1.0)
        return result

function = FunctionCalculator()
print(function.calculate(10, 20))
print(function.calculate(100, 120))
print(function.calculate(1000, 1200))
print(function.calculate(10000, 10200))

