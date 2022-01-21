## @file Shape.py
#  @author Rithvik Bhogadi
#  @brief Defining different shapes for different physical objects
#  @date 02/16/2021

from abc import ABC, abstractmethod

## @brief Shapes provides an interface for circles, triangles and different types of shapes
## @details The method in the interface are abstract and need to be
#  overridden by the modules that inherit this interface


class Shape(ABC):

    @abstractmethod
    ## @brief a method which provides the x coordinate of the center mass
    def cm_x(self):
        pass

    @abstractmethod
    ## @brief a method which provides the y coordinate of the center mass
    def cm_y(self):
        pass
    
    @abstractmethod
    ## @brief a method which provides a mass
    def mass(self):
        pass

    @abstractmethod
    ## @brief a method that provides the inertia of the object
    def m_inert(self):
        pass

        
