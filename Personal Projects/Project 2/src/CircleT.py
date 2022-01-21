## @file CircleT.py
#  @author Rithvik Bhogadi
#  @brief a module interface which inherits Shape.py and provides a CircleT shape object
#  @date 02/16/2021

from Shape import Shape

class CircleT(Shape):

    ## @brief constructor for class CircleT,
    # which consists of different parts of the object
    #  @param x represents the x coordinate of the shape
    #  @param y reprents the y coordinate of the shape
    #  @param r represents the radius of the shape
    #  @param m represents the mass of the shape
    def __init__(self, x, y, r, m):
        if not r > 0 and m > 0:
            raise ValueError
        self.x = x
        self.y = y
        self.r = r
        self.m = m


    ## @brief calculates the x coordinate of the shape
    #  @return return the x coordinate for CircleT
    def cm_x(self):
        return self.x

    ## @brief calculates the y coordinate of the shape
    #  @return return the y coordinate for CircleT
    def cm_y(self):
        return self.y

    ## @brief calculates the mass of the object
    #  @return returns the mass of the object
    def mass(self):
        return self.m

    ## @brief calculates the moment of inertia of the object
    #  @return returns the moment of inertia of the object
    def m_inert(self):
        return ((self.m*(self.r*self.r))/2)

