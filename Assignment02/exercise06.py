import numpy as np
class DataAnalyser:
    def __init__(self, data):
        self.data = [np.random.rand() for i in range(data)]

    def sum(self):
        return sum(self.data)

    def product(self):
        p = 1
        for i in self.data:
            p *= i
        return p

    def average(self):
        return np.average(self.data)

    def variance(self):
        return np.var(self.data)

    def minimum(self):
        return min(self.data)

    def maximum(self):
        return max(self.data)

n1 = 0
while not (n1 > 0 and n1 <= 1000000):
    n1 = input('Enter n1 between 0 to 1000000: ')
n2 = input('Enter n2: ')
n3 = n2 + 1
while n3 >= n2:
    n3 = input('Enter n3 which is less than n2: ')
data_analyzer = DataAnalyser(n1)
print('Sum:', data_analyzer.sum())
print('Product:', data_analyzer.product())
print('Average:', data_analyzer.average())
print('Variance:', data_analyzer.variance())
print('Minimum:', data_analyzer.minimum())
print('Maximum:', data_analyzer.maximum())

