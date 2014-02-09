# This program is free software. It comes without any warranty, 
# to the extent permitted by applicable law. You can redistribute 
# it and/or modify it under the terms of the Do What The Fuck You 
# Want To Public License, Version 2, as published by Sam Hocevar. 
# See http://sam.zoy.org/wtfpl/COPYING for more details. 

import math

class Vector4:
	def __init__(self,e=[0.0,0.0,0.0,0.0]):
		if (len(e) != 4):
			raise ValueError('attempted to initialize 4-vector from list of inappropriate length')
		self.e = [float(e[i]) for i in range(4)]
	def __add__(self,other):
		return Vector4([self.e[i]+other.e[i] for i in range(4)])
	def __sub__(self,other):
		return Vector4([self.e[i]-other.e[i] for i in range(4)])
	def __rmul__(self,scalar):
		return Vector4([scalar*self.e[i] for i in range(4)])
	def __str__(self):
		return str(self.e)
	
def dotproduct(v1,v2):
	result = 0.0
	for i in range(4):
		result += v1.e[i]*v2.e[i]
	return result

def crossproduct(v1,v2):
	result = [0.0,0.0,0.0,0.0]
	result[0] = v1.e[1]*v2.e[2] - v1.e[2]*v2.e[1]
	result[1] = v1.e[2]*v2.e[0] - v1.e[0]*v2.e[2]
	result[2] = v1.e[0]*v2.e[1] - v1.e[1]*v2.e[0]
	result[3] = 0.0
	return Vector4(result)

def matr_vec_mul2(m, v):
	if (len(m) != len(v)):
		raise TypeError('attempted to multiply matrix with vector of inappropriate dimension')
	result = [0.0 for i in range(len(m[0]))]
	for i in range(len(m[0])):
		for j in range(len(m)):
			result[i] += m[j][i]*v[j]
	return result

class Matrix4x4:
	def __init__(self, e=[[0.0,0.0,0.0,0.0],[0.0,0.0,0.0,0.0],[0.0,0.0,0.0,0.0],[0.0,0.0,0.0,0.0]]):
		if (len(e) != 4) or (len(e[0]) != 4):
			raise ValueError('attempted to initialize 4x4-matrix from list of inappropriate dimensions')
		self.e = [[float(e[j][i]) for i in range(len(e[j]))] for j in range(len(e))]
	def __add__(self,other):
		return Matrix4x4([[self.e[j][i]+other.e[j][i] for i in range(len(self.e[j]))] for j in range(len(self.e))])
	def __sub__(self,other):
		return Matrix4x4([[self.e[j][i]-other.e[j][i] for i in range(len(self.e[j]))] for j in range(len(self.e))])
	def __mul__(self,other):
		return Matrix4x4([matr_vec_mul2(self.e,column) for column in other.e])
	def __str__(self):
		return str(self.e)

def matr_vec_mul(m,v):
	return Vector4(matr_vec_mul2(m.e,v.e))

# returns a 4x4 identity matrix
def identity():
	return Matrix4x4([[1.0,0.0,0.0,0.0],[0.0,1.0,0.0,0.0],
		[0.0,0.0,1.0,0.0], [0.0,0.0,0.0,1.0]])

# returns a 4x4 translation matrix
def translate(x,y,z):
	m = identity()
	m.e[3] = [x,y,z,1.0]
	return m

# returns a 4x4 rotation matrix 
# rotates about the x-axis
def rot_x(angle):
	c = math.cos(angle)
	s = math.sin(angle)
	m = identity()
	m.e[1] = [0.0,c,s,0.0]
	m.e[2] = [0.0,-s,c,0.0]
	return m
# as above, about the y-axis
def rot_y(angle):
	c = math.cos(angle)
	s = math.sin(angle)
	m = identity()
	m.e[0] = [c,0.0,-s,0.0]
	m.e[2] = [s,0.0,c,0.0]
	return m
# as above, about the z-axis
def rot_z(angle):
	c = math.cos(angle)
	s = math.sin(angle)
	m = identity()
	m.e[0] = [c,s,0.0,0.0]
	m.e[1] = [-s,c,0.0,0.0]
	return m

# returns a perspective projection matrix,
# projects onto the plane z=1.0, with the origin as center of projection
def projection():
	m = identity()
	m.e[2] = [0.0,0.0,0.0,1.0]
	m.e[3] = [0.0,0.0,1.0,0.0]
	return m

# returns a viewport matrix (translates from a coordinate system with origin 
# at the center of the screen to one with center at the top-left corner of the screen, 
# and with y-axis pointing downwards - this is the one used by pygame for drawing). 
def viewport(screen_width, screen_height,fov):
	scale = max(screen_width,screen_height)/(2.0*math.tan(fov/2.0))
	xcenter = screen_width/2.0
	ycenter = screen_height/2.0

	m = identity()
	m.e[0] = [scale,0.0,0.0,0.0]
	m.e[1] = [0,-scale,0.0,0.0]
	m.e[3] = [xcenter,ycenter,0.0,1.0]
	return m
