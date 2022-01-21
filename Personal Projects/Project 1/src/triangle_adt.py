## @file triangle_adt.py
#  @author Rithvik Bhogadi
#  @brief Contains a class for working with Triangles
#  @date 01/21/2021


import math
import cmath
from enum import Enum

## @brief An ADT for different types of triangles
#  @details A TriType is made up a different types of triangles
class TriType(Enum):
    equilat = 1
    isosceles = 2
    scalene = 3
    right = 4

## @brief An ADT for triangles and their components
#  @details A triangle is composed of three lengths
class TriangleT:

  ## @brief Constructor for TriangleT
  #  @details Creates a triangle based on three side lengths
  #  @param l1 Integer representing one of the side lengths of a triangle
  #  @param l2 Integer representing one of the side lengths of a triangle
  #  @param l3 Integer representing one of the side lengths of a triangle
  def __init__(self, l1, l2, l3):
    self.l1 = l1
    self.l2 = l2
    self.l3 = l3
    
  ## @brief Gets the side lengths of the triangle
  #  @return returns a tuple, where each integer is the length of one side of the triangle
  def get_sides(self):
    return (self.l1, self.l2, self.l3)

  ## @brief checks to see if two triangle are equal to each other
  #  @param argument A second triangle object
  #  @return returns true if both triangles are equal to each other, otherwise it returns false
  def equal(self, argument):
    if self.l1 > 0 and self.l2 > 0 and self.l3 > 0:
      if argument.l1 > 0 and argument.l2 > 0 and argument.l3 > 0:
        if self.l1 == argument.l1 and self.l2 == argument.l2 and self.l3 == argument.l3:
            return True
    else:
        return False

  ## @brief calculates the perimeter of the triangle
  #  @return returns an integer representing the perimeter of the current triangle
  def perim(self):
    length_one = self.l1
    length_two = self.l2
    length_three = self.l3
    sum_one = (length_one + length_two + length_three)
    if length_one > 0 and length_two > 0 and length_three > 0:
        return sum_one
    else:
        return False

  ## @brief calculates the area of the triangle
  #  @return returns a float representing the area of the current triangle
  def area(self):
    length_o1 = self.l1
    length_o2 = self.l2
    length_o3 = self.l3
    semi_p = (length_o1 + length_o2 + length_o3)/2
    ar_o1 = (semi_p * (semi_p - length_o1) * (semi_p - length_o2) * (semi_p - length_o3)) ** 0.5
    if length_o1 > 0 and length_o2 > 0 and length_o3 > 0:
        return ar_o1

  ## @brief checks to see whether the triangle is a valid triangle or not
  #  @return returns true if the triangle is a valid triangle, otherwise it will return false
  def is_valid(self):
    valid_l1 = self.l1
    valid_l2 = self.l2
    valid_l3 = self.l3
    if valid_l1 > 0 and valid_l2 > 0 and valid_l3 > 0:
        if ((valid_l1 + valid_l2) > valid_l3) and ((valid_l2 + valid_l3) > valid_l1) and ((valid_l1 + valid_l3) > valid_l2):
            return True
    else:
        return False

  ## @brief Checks to see what type of triangle the triangle is
  # @details Assuming that this method will only return a single unique type of triangle rather than multple as per the syntax
  #  @return returns the type of triangle such as equilateral, isosceles, scalene or right angle triangle
  def tri_type(self):
    tri_l1 = self.l1
    tri_l2 = self.l2
    tri_l3 = self.l3
    do_l1 = math.pow(tri_l1, 2)
    do_l2 = math.pow(tri_l2, 2)
    do_l3 = math.pow(tri_l3, 2)
    if tri_l1 > 0 and tri_l2 > 0 and tri_l3 > 0: 
        if tri_l1 == tri_l2 and tri_l2 == tri_l3:
            return TriType.equilat
        lister = [do_l1, do_l2, do_l3]
        lister.sort()
        if ((lister[0] + lister[1]) == lister[2]):
            return TriType.right
        if ((tri_l1 == tri_l3) != tri_l2) or ((tri_l2 == tri_l3) != tri_l1):
            return TriType.isosceles
        if tri_l1 != tri_l2 and tri_l1 != tri_l3 and tri_l2 != tri_l3:
            return TriType.scalene
    else:
        return False
    
  

