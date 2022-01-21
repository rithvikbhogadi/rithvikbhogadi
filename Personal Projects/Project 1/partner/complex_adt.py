## @file complex_adt.py
#  @author Shiraz Masliah
#  @title Step 1
#  @date January 28th, 2021

##  @brief Going based off of the assumption that all inputs are correct and computable
#   An assumption that a value of zero will not be supplied

import cmath
import numpy as np

class ComplexT:

	## @brief ComplexT constructor
	#  @details Initializes ComplexT object with real, imaginary and complex numbers
	#  @params x The real part of the complex number
	#  @params y The imaginary part of the complex number
	def __init__(self, x, y):
		self.x = x
		self.y = y
		self.z = complex(self.x, self.y)

	## @brief Getter for the real part of the complex number
	#  @return Real part of complex number (x)
	def real(self):
		return (self.x)

	## @brief Getter for the imaginary part of the complex number
	#  @return Imaginary part of complex number (y)
	def imag(self):
		return (self.y)

	## @brief Getter for the complex number
	#  @return The complex number
	def get_z(self):
		return (self.z)

	## @brief Getter for the absolute value of the complex number
	#  @return Absolute value of complex number	
	def get_r(self):
		return (abs(self.z))

	## @brief Returns phase of complex number in radians
	#  @details Ranges from -pi to pi, and rounds to 3 decimal places
	#  @return Phase of complex number
	def get_phi(self):
		phi = cmath.phase(self.z)
		return (round(phi, 3))

	## @brief Checks equality of two complexTs
	#  @return boolean True or False
	def equal(self, complexT):
		return (self.z == complexT.z)

	## @brief Returns the conjugate of a complex number
	#  @return the conjugate of the complex number
	def conj(self):
		return (np.conj(self.z))

	## @brief Adds two complex numbers together
	#  @return the sum of the argument and current object
	def add(self, complexT):
		complex_num = self.z + complexT.z
		return ComplexT(complex_num.real, complex_num.imag)

	## @brief Subtracts argument from current object
	#  @return the difference of the argument and current object
	def sub(self, complexT):
		complex_num = self.z - complexT.z
		return ComplexT(complex_num.real, complex_num.imag)

	## @brief Multiplies argument and current object
	#  @return the product of the argument and current object
	def mult(self, complexT):
		complex_num = self.z * complexT.z
		return ComplexT(complex_num.real, complex_num.imag)

	## @brief Finds the reciprocal of the current object
	#  and rounds to 3 decimal places
	#  @return the reciprocal of a complex number
	def recip(self):
		return (np.round((np.reciprocal(self.z)),3))

	## @brief Divides current object by argument
	#  @return the divided complex number
	def div(self, complexT):
		return (self.z / complexT.z)

	## @brief Finds the square root of the current object
	#  and rounds to 3 decimal places
	#  @return the positive square root of the complex number
	def sqrt(self):
		return (np.round((cmath.sqrt(self.z)),3))
