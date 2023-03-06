""" 
        part 1
    -iterate through the string equation scanned from the user
    -check teh string if it contains backslashes to call fractions function
    - prprogram must be able to identify: eeulers, ppi,numbers/ deciamls


"""

import fractions
import numpy as np
class Main:
    def __init__ (self,x ,y):
        self.equation = []
        self.nums = {1,2,3,4,5,6,7,8,9,0}
        self.num1 = x
        self.num2 = y

    def relative_error(self, tv, av):
        """ formula for relative error is
            abs of (tv - av)/tv
            then we muliply it to 100
        """
        temp = (tv - av)/tv

        res = np.absolute(temp)
        return res
    def rounding(self,num):
        return 0
    def chopping(self, num):
        return 0
    def euler (self, num):
        return 0
    def fraction(self, numerator, denaminator):
        return 0
    