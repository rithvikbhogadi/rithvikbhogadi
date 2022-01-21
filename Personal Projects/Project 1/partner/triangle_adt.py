## @file triangle_adt.py
#  @author Shiraz Masliah
#  @title Step 2
#  @date January 21st, 2021

## @details Going based off of the assumption that all inputs are correct and computable

from enum import Enum 

class TriType:
	#  @details enum variables
	right = 0
	equilat = 1
	isosceles = 2
	scalene = 3

## @brief This class represents a triangle
#  @details This class represents a triangle as (a, b, c)
#  where each is a side of the triangle
class TriangleT:

	#  @param python convention is to put double underscore before the identifier
	def __init__(self, a, b, c):
	#  private variables, each a side length
		self.a = a
		self.b = b
		self.c = c

	## @brief Returns the side lengths
	#  @return tuple of integers, each the length of one side of the triangle
	def get_sides(self):
		return (self.a, self.b, self.c)

	## @brief Checks if two triangles are the same
	#  @return true if TriangleT is equal to the argument
	def equal(self, triangleT):
		selfList = [self.a, self.b, self.c]
		triangleTList = [triangleT.a, triangleT.b, triangleT.c]
		selfList.sort()
		triangleTList.sort()
		return (selfList == triangleTList)

	## @brief This function calculates the perimeter of the given triangle
	#  @return perimeter of triangle
	def perim(self):
		return (self.a + self.b + self.c)

	## @brief This function calculates the area of the given triangle
	#  @detail rounded to 3 decimal places
	#  @return area of triangle
	def area(self):
		s = (self.a + self.b + self.c) / 2
		return (round(float((s*(s-self.a)*(s-self.b)*(s-self.c))**0.5),3))

	## @brief This function checks if the triangle is valid by making sure the sum of two sides
	## is greater than the third
	#  @return True if the 3 sides form a valid triangle
	def is_valid(self):
		if self.a + self.b > self.c and self.b + self.c > self.a and self.c + self.a > self.b:
			return True
		else:
			return False

	#  @return the type of triangle
	#  @param prioritizes right angle triangles
	def tri_type(self):
		x, y, z = self.a ** 2, self.b ** 2, self.c ** 2
		if max(x, y, z) == (x + y + z - max(x, y, z)):
			return TriType.right
		elif(self.a == self.b and self.b == self.c and self.a == self.c):
			return TriType.equilat
		elif(self.a == self.b or self.b == self.c or self.a == self.c):
			return TriType.isosceles
		else:
			return TriType.scalene



