## @file BodyT.py
#  @author Shiraz Masliah
#  @date February 16, 2021

from Shape import Shape


#  @brief BodyT is a subclass of Shape
class BodyT(Shape):

    def __init__(self, x, y, m):

        #  @details Raises value error if the lengths
        #  of each list are not equal
        if not(len(x) == len(y) and len(y) == len(m)):
            raise ValueError("Lists not of equal lengths")
        #  @details Raises value error if any value in list m
        #  are less than zero
        for i in m:
            if not (i > 0):
                raise ValueError("m > 0")

        #  @details Initialized circle objects
        #  @params cmx, cmy, sum, and moment
        self.cmx = self.cm(x, m)
        self.cmy = self.cm(y, m)
        self.m = self.sum(m)
        squared = ((self.cm(x, m))**2 + (self.cm(y, m))**2)
        self.moment = self.mmom(x, y, m) - (self.sum(m)) * squared

    ## @brief Method for getting a number
    #  @returns cmx
    def cm_x(self):
        return self.cmx

    ## @brief Method for getting a number
    #  @returns cmy
    def cm_y(self):
        return self.cmy

    ## @brief Method for getting a number
    #  @returns mass
    def mass(self):
        return self.m

    ## @brief Method for getting a number
    #  @returns Moment of inertia
    def m_inert(self):
        return (self.moment)

    # @details local functions

    ## @brief Method adding numbers in list m
    #  @returns Summation of numbers in list m
    def sum(self, m):
        summation = 0
        for r in m:
            summation += r
        return summation

    ## @brief Method for finding cm
    #  @returns The multiple of each number in two lists
    #  and divides the product by the sum of all numbers in
    #  list m
    def cm(self, z, m):
        result = 0
        for i in range(len(m)):
            result += z[i] * m[i]
        return result / sum(m)

    ## @brief Method for finding the moment
    #  @returns the multiple of m by x and y squared
    #  for each number in each list
    def mmom(self, x, y, m):
        result = 0
        for i in range(len(m)):
            result += m[i] * (x[i]**2 + y[i]**2)
        return result
