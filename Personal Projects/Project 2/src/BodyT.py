## @file BodyT.py
#  @author Rithvik Bhogadi
#  @brief Provides a sequence of mass in space
#  @date 02/16/2021

from Shape import Shape

class BodyT(Shape):

    ## @brief constructor for class BodyT
    #  @param cmx1 A x coordinate of the BodyT
    #  @param cmy1 A y coordinate of the BodyT
    #  @param m1 Provides one of the masses of BodyT
    def __init__(self, cmx1, cmy1, m1):
        
        def mmom(x,y,m):
            addo = [(m[i] * (x[i] ** 2 + y[i] ** 2)) for i in range(len(m))]
            return sum(addo)
        
        def cm(z,m):
            diver = [z[i] * m[i] for i in range(len(m))]
            return sum(diver) / sum(m)
        
        if not len(cmx1) == len(cmy1) == len(m1):
            raise ValueError
        self.cmx = cm(cmx1,m1)
        self.cmy = cm(cmy1,m1)
        self.m = sum(m1)
        self.moment = mmom(cmx1, cmy1, m1) - (self.m * (self.cmx ** 2 + self.cmy ** 2))


    ## @brief calculates the x coordinate of the shape
    #  @return return the x coordinate for BodyT
    def cm_x(self):
        return self.cmx

    ## @brief calculates the y coordinate of the shape
    #  @return return the x coordinate for BodyT
    def cm_y(self):
        return self.cmy

    ## @brief calculates the mass of the object
    #  @return return the mass of the object
    def mass(self):
        return self.m

    ## @brief calculates the moment of inertia of the object
    #  @return return the moment of inertia of the object
    def m_inert(self):
        return self.moment
