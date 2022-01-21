## @file TriangleT.py
#  @author Shiraz Masliah
#  @date February 16, 2021

from Shape import Shape


#  @brief TriangleT is a subclass of Shape
class TriangleT(Shape):

    ## @brief Triangle constructor
    def __init__(self, x, y, s, m):

        #  @details Raises value error if s is less than zero
        if not(s > 0):
            raise ValueError("s value must be greater 0")
        #  @details Raises value error if the mass is less than zero
        if not(m > 0):
            raise ValueError("mass value must be greater 0")

        #  @details Initialized triangle objects
        #  @params x, y, s, and mass
        self.x = x
        self.y = y
        self.s = s
        self.m = m

    ## @details Overrides Shape class method
    #  @returns Moment of inertia
    def m_inert(self):
        return ((self.m * (self.s**2)) / 12)
