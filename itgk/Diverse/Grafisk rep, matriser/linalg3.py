# This program is free software. It comes without any warranty, 
# to the extent permitted by applicable law. You can redistribute 
# it and/or modify it under the terms of the Do What The Fuck You 
# Want To Public License, Version 2, as published by Sam Hocevar. 
# See http://sam.zoy.org/wtfpl/COPYING for more details. 

import math

class Vector3:
	def __init__(self,e=[0.0,0.0,0.0]):
		if (len(e) != 3):
			raise ValueError('attempted to initialize 4-vector from list of inappropriate length')
		self.e = [float(e[i]) for i in range(3)]
	def __add__(self,other):
		return Vector3([self.e[i]+other.e[i] for i in range(3)])
	def __sub__(self,other):
		return Vector3([self.e[i]-other.e[i] for i in range(3)])
	def __rmul__(self,scalar):
		return Vector3([scalar*self.e[i] for i in range(3)])
	def __str__(self):
		return str(self.e)

def matr_vec_mul2(m, v):
	if (len(m) != len(v)):
		raise TypeError('attempted to multiply matrix with vector of inappropriate dimension')
	result = [0.0 for i in range(len(m[0]))]
	for i in range(len(m[0])):
		for j in range(len(m)):
			result[i] += m[j][i]*v[j]
	return result

class Matrix3x3:
	def __init__(self, e=[[0.0,0.0,0.0],[0.0,0.0,0.0],[0.0,0.0,0.0]]):
		if (len(e) != 3) or (len(e[0]) != 3):
			raise ValueError('attempted to initialize 3x3-matrix from list of inappropriate dimensions')
		self.e = [[float(e[j][i]) for i in range(len(e[j]))] for j in range(len(e))]
	def __add__(self,other):
		return Matrix3x3([[self.e[j][i]+other.e[j][i] for i in range(len(self.e[j]))] for j in range(len(self.e))])
	def __sub__(self,other):
		return Matrix3x3([[self.e[j][i]-other.e[j][i] for i in range(len(self.e[j]))] for j in range(len(self.e))])
	def __mul__(self,other):
		return Matrix3x3([matr_vec_mul2(self.e,column) for column in other.e])
	def __str__(self):
		return str(self.e)

def matr_vec_mul(m,v):
	return Vector3(matr_vec_mul2(m.e,v.e))

# returns a 3x3 identity matrix
def identity():
	return Matrix3x3([[1.0,0.0,0.0],[0.0,1.0,0.0],[0.0,0.0,1.0]])

# returns a 3x3 translation matrix
def translate(x,y):
	m = identity()
	m.e[2] = [x,y,1.0]
	return m
# returns a 3x3 rotation matrix 
def rot(angle):
	c = math.cos(angle)
	s = math.sin(angle)
	m = identity()
	m.e[0] = [c,s,0.0]
	m.e[1] = [-s,c,0.0]
	return m

# returns a 3x3 scale matrix
def scale(xscale,yscale):
	m = identity()
	m.e[0] = [xscale,0.0,0.0]
	m.e[1] = [0.0,yscale,0.0]
	return m
# returns a viewport matrix (translates from a coordinate system with origin 
# at the center of the screen to one with center at the top-left corner of the screen, 
# and with y-axis pointing downwards - this is the one used by pygame for drawing). 
def viewport(screen_width,screen_height):
	s = max(screen_width,screen_height)/2.0
	m = translate(screen_width/2.0,screen_height/2.0)*scale(s,-s)
	return m