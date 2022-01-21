## @file Scene.py
#  @author Shiraz Masliah
#  @date February 16, 2021

#  @brief CircleT is a subclass of Shape
#  @details uses library SciPy
from Shape import Shape
import scipy.integrate as spy


## @brief Scene constructor
class Scene(Shape):

    #  @details Initialized scene objects
    #  @params s, fx, fy, vx, and vy
    def __init__(self, s, fx, fy, vx, vy):
        self.s = s
        self.fx = fx
        self.fy = fy
        self.vx = vx
        self.vy = vy

    ## @brief Method for getting a number
    #  @returns s
    def get_shape(self):
        return self.s

    ## @brief Method for getting fx and fy
    #  @returns fx and fy
    def get_unbal_forces(self):
        return (self.fx, self.fy)

    ## @brief Method for getting vx and vy
    #  @returns vx and vy
    def get_init_velo(self):
        return (self.vx, self.vy)

    ## @brief Method defining s
    #  @returns s
    def set_shape(self, s):
        self.s = s

    ## @brief Method defining fx and fy
    def set_unbal_forces(self, fx, fy):
        self.fx = fx
        self.fy = fy

    ## @brief Method defining vx and vy
    def set_init_velo(self, vx, vy):
        self.vx = vx
        self.vy = vy

    ## @brief Method calculates the sim
    #  @returns t and ode list
    def sim(self, tfinal, nsteps):
        t = []
        for i in range(nsteps):
            t.append(i * tfinal / (nsteps - 1))
        return (t, spy.odeint(self.ode, [self.s.cm_x(), self.s.cm_y(), self.vx, self.vy], t))

    ## @brief Local function
    ## @returns a ode list
    def ode(self, w, t):
        result = [w[2], w[3], (self.fx(t) / self.s.mass()), (self.fy(t) / self.s.mass())]
        return result
