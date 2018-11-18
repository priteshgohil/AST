#!/usr/bin/env python
# coding: utf-8

class FunctionCalculator:
    def __init__(self):
        pass
    
    def calculate(self, intermediate, Iterations):
        r = 1
        for i in range(1, Iterations + 1):
            v = 0
            if i == 1:
                v = .5
            elif i > 1 and i < intermediate:
                v = .9
            elif i >= intermediate:
                v = .1
            r *= v / (1 - v)
        return (1.0 - ((1.0 + r)**(-1)))
    
function = FunctionCalculator()
# In[ ]:




