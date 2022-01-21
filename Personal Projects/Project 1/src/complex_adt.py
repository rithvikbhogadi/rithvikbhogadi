## @file complex_adt.py
#  @author Rithvik Bhogadi
#  @brief Contains a class for working with complex numbers
#  @date 01/21/2021

import math
import cmath

## @brief An ADT for complex numbers
#  @details A complex is composed of a real and imaginary part
class ComplexT:

  ## @brief Constructor for ComplexT
  #  @details Creates a complex number based on a given x and y float values
  #  @param self representing the created ComplexT object
  #  @param x Integer representing the real float value
  #  @param y Integer representing the imaginary float value
  def __init__(self, x, y):
    self.x = x
    self.y = y
    
  ## @brief Gets the real part of the complex number
  #  @return Integer representing the real part of the complex number
  def real(self):
    return self.x

  ## @brief Gets the imaginary part of the complex number
  #  @return Integer representing the imaginary part of the complex number
  def imag(self):
    return self.y

  ## @brief Gets the absolute value of a complex number
  #  @return Integer representing the modulus of a complex number
  def get_r(self):
    real_r = math.pow(self.x, 2)
    imag_r = math.pow(self.y, 2)
    return math.sqrt(real_r + imag_r)

  ## @brief Returns the phase of a complex number
  #  @return return the phase of a complex number in radians
  def get_phi(self):
    return cmath.phase(complex(self.y, self.x))

  ## @brief compares the equivalence between two complex numbers
  # @param argument The argument of ComplexT
  #  @return returns true or false depending on the comparison between two complex numbers
  def equal(self, argument):
    if argument.x == self.x and argument.y == self.y:
        return True
    else:
        return False

  ## @brief Find the complex conjugate of the complex number
  #  @return returns the complext conjugate of the current object
  def conj(self):
    conj_x = self.x
    conj_y = (self.y * -1)
    return ComplexT(conj_x, conj_y)

  ## @brief Adds two complex numbers together
  #  @param argument A complex number
  #  @return returns the sum of two complex numbers
  def add(self, argument):
    add_x = self.x + argument.x
    add_y = self.y + argument.y
    return ComplexT(add_x, add_y)

  ## @brief subtracts two complex number
  #  @param Argument A complex number
  #  @return return the difference in the form of a complex number
  def sub(self, argument):
    sub_x = self.x - argument.x
    sub_y = self.y - argument.y
    return ComplexT(sub_x, sub_y)

  ## @brief Performs the multiplication between two complex numbers
  #  @param Argument A complex number
  #  @return return the product after the multiplication
  def mult(self, argument):
    mult_x = self.x
    mult_y = self.y
    multo_x = argument.x
    multo_y = argument.y
    multa = mult_x * multo_x
    multay = mult_y * multo_y
    multa2 = mult_x * multo_y
    multay2 = mult_y * multo_x
    mult_ul = multa - multay
    mult_ul2 = multa2 + multay2
    return ComplexT(mult_ul, mult_ul2)

  ## @brief Performs the reciprocal of a complex number
  #  @return return the reciprocal of a complex number 
  def recip(self):
    recip_x = self.x
    recip_y = (self.y * -1)
    recip_powx = math.pow(self.x, 2)
    recip_powy = math.pow(self.y, 2)
    recip_x1 = (recip_x/(recip_powx + recip_powy))
    recip_y1 = (recip_y/(recip_powx + recip_powy))
    return ComplexT(recip_x1, recip_y1)

  ## @brief Performs the division between two complex numbers
  #  @param Argument A complex number
  #  @return return the product after the multiplication
  def div(self, argument):
    div_xy = argument.recip()
    return self.mult(div_xy)
  
  ## @brief Performs the square root of a complex number
  #  @return return the positive square root of the current object
  def sqrt(self):
    sqrt_x = self.x
    sqrt_y = self.y
    sqrt_xy = cmath.sqrt(complex(sqrt_x, sqrt_y))
    return ComplexT(sqrt_xy.real, sqrt_xy.imag)