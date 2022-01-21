## @file TriangleT.py
#  @author Rithvik Bhogadi
#  @brief a module interface which inherits Shape.py and provides a TriangleT shape object
#  @date 02/16/2021

from Shape import Shape

class TriangleT(Shape):

    ## @brief constructor for class TriangleT
    #  @param x represents the x coordinate
    #  @param y represents the y coordinate
    #  @param s represents the side length
    #  @param m represents the mass
    def __init__(self, x, y, s, m):
        if not s > 0 and m > 0:
            raise ValueError
        self.x = x
        self.y = y
        self.s = s
        self.m = m


    ## @brief calculates the x coordinate of the shape
    #  @return return the x coordinate for TriangleT
    def cm_x(self):
        return self.x

    ## @brief calculates the y coordinate of the shape
    #  @return return the y coordinate for TriangleT
    def cm_y(self):
        return self.y

    ## @brief calculates the mass of the object
    #  @return return the mass of the object
    def mass(self):
        return self.m

    ## @brief calculates the moment of inertia of the object
    #  @return returns the mmoment of inertia of the object
    def m_inert(self):
        return ((self.m*(self.s*self.s))/12)
