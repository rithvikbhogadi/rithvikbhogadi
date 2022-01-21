## @file CircleT.py
#  @author Shiraz Masliah
#  @date February 16, 2021

from Shape import Shape


#  @brief CircleT is a subclass of Shape
class CircleT(Shape):

    ## @brief Circle constructor
    def __init__(self, x, y, r, m):

        #  @details Raises value error if the radius is less than zero
        if not(r > 0):
            raise ValueError("radius value must be greater 0")
        #  @details Raises value error if the mass is less than zero
        if not(m > 0):
            raise ValueError("mass value must be greater 0")

    #  @details Initialized circle objects
    #  @params x, y, radius, and mass
        self.x = x
        self.y = y
        self.r = r
        self.m = m
