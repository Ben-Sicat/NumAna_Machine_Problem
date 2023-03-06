import numpy as np
import fractions
import math

class calculations:
    def __init__(self):
        self.attribute = "Hello"
        self.relative_chopped = 0
        self.relative_rounded = 0
        
    def euler_num(self, exponent):
        temp = np.exp(exponent)
        return temp
    def pi_num(self,exponent):
        temp = np.pi(exponent)
        return temp  
    def relative_error(self, t_value, a_value):
        r_error = np.absolute((t_value - a_value)/t_value)
        r_error *= r_error
        return r_error

    def chopped(self,num, x):
        chopped_num = math.floor(num * (10**x) / (10 ** x))
        return chopped_num
    
    def rounded(self,num, x):
        rounded_num = round(num, x)
        return rounded_num
    







