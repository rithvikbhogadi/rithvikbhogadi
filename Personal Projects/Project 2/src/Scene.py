## @file Scene.py
#  @author Rithvik Bhogadi
#  @brief A module interface which gets/sets shapes,unbalanced forces and initial velocities
#  @date  02/16/2021

from Shape import Shape
from scipy.integrate import odeint


class Scene():

    ## @brief constructor for class Scene
    #  @param s represents Shape
    #  @param Fx represnts the unbalanced force function in x dir
    #  @param Fy represents the unbalanced force function y dir
    #  @param vx represents the initial velocity in x dir
    #  @param vy represents the initial velocity in y dir
    def __init__(self,s,Fx,Fy,vx,vy):
        
        self.s = s
        self.Fx = Fx
        self.Fy = Fy
        self.vx = vx
        self.vy = vy


    ## @brief gets the shape of the object
    #  @return returns the shape of the object
    def get_shape(self):
        return self.s

    ## @brief gets the unbalanced forces of the shape
    #  @return returns the unbalanced forces in the x and y dir
    def get_unbal_forces(self):
        return self.Fx, self.Fy

    ## @brief gets the initial velocity of the shape
    #  @return returns the initial velocities in the x and y dir
    def get_init_velo(self):
        return self.vx, self.vy

    ## @brief sets the shape
    #  @param s the shape of the object
    #  @return returns the newly set shape of the object
    def set_shape(self, s):
        self.s = s
        
    ## @brief sets the unbalanced forces in x dir and y dir
    #  @param Fx the force of the object in the x dir
    #  @param Fy the force of the object in the y dir
    #  @return returns the newly set forces of the object in the x dir and y dir
    def set_unbal_forces(self, Fx, Fy):
        self.Fx = Fx
        self.Fy = Fy
        
    ## @brief sets the initial velocities in x dir and y dir
    #  @param vx the initial velocity of the object in the x dir
    #  @param vy the initial velocity of the object in the y dir
    #  @return returns the newly set velocities of the object in the x dir and y dir
    def set_init_velo(self, vx, vy):
        self.vx = vx
        self.vy = vy
    
    def ode(self,w,t):
        return [w[2],w[3],self.Fx(t)/self.s.mass(),self.Fy(t)/self.s.mass()]
    
    ## @brief Simulating the different shapes
    #  @param t_final represents the final sequence of numbers
    #  @param n_steps represents the number of steps
    #  @return returns a sequence of numbers
    def sim(self,t_final,n_steps):
        t = []
        for i in range(n_steps):
            t.append((i*t_final)/(n_steps-1))
        return t, odeint(self.ode, [self.s.cm_x(),self.s.cm_y(),self.vx,self.vy], t)
        