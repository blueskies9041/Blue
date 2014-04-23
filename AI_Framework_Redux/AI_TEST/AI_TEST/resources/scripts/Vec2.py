import math
from math import sqrt, pow, sin, cos

## Vec2 Class ##
class Vec2:
# __init__ is a special "constructor" esque function, must have self as first arg
	def __init__( self, _x, _y): 
		self.x = _x
		self.y = _y	
	def mag(self):
		return sqrt((self.x**2) + (self.y**2))
	def normal(self):
		if self.mag() > 0:
			return Vec2( self.x / self.mag(), self.y / self.mag() )
		else:
			return self
	def normalize(self):
		if self.mag() > 0:
			self.x /= self.mag()
			self.y /= self.mag()
		else:
			pass
	def distance(self, _otherVec):
		return sqrt( pow( (_otherVec.x - self.x) , 2) + pow( (_otherVec.y - self.y), 2))
	def __sub__(self, other):
		return Vec2( self.x - other.x, self.y - other.y)
	def __add__(self, other):
		return Vec2( self.x + other.x, self.y + other.y)
	def __mul__(self, scalar):
		return Vec2( self.x * scalar, self.y * scalar)
	def set_by_angle(self, angle):
		self.x = sin(angle) * self.mag()
		self.y = cos(angle) * self.mag()
	def getstr(self):
		return str( (self.x, self.y))
