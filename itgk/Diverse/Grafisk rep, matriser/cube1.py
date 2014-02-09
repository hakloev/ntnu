# This program is free software. It comes without any warranty, 
# to the extent permitted by applicable law. You can redistribute 
# it and/or modify it under the terms of the Do What The Fuck You 
# Want To Public License, Version 2, as published by Sam Hocevar. 
# See http://sam.zoy.org/wtfpl/COPYING for more details. 

import sys,math,pygame,copy

from linalg4 import *

class Application:
	def __init__(self,scr_width=640,scr_height=480,animate=1):
		pygame.init()
		# initialize a 3D object
		self.obj = [[Vector4([-1.0,1.0,-1.0,1.0]), Vector4([1.0,1.0,-1.0,1.0]), Vector4([1.0,-1.0,-1.0,1.0]), Vector4([-1.0,-1.0,-1.0,1.0])],
			[Vector4([1.0,1.0,1.0,1.0]), Vector4([-1.0,1.0,1.0,1.0]), Vector4([-1.0,-1.0,1.0,1.0]), Vector4([1.0,-1.0,1.0,1.0])],
			[Vector4([1.0,1.0,-1.0,1.0]), Vector4([1.0,1.0,1.0,1.0]), Vector4([1.0,-1.0,1.0,1.0]), Vector4([1.0,-1.0,-1.0,1.0])],
			[Vector4([-1.0,1.0,1.0,1.0]), Vector4([-1.0,1.0,-1.0,1.0]), Vector4([-1.0,-1.0,-1.0,1.0]), Vector4([-1.0,-1.0,1.0,1.0])],
			[Vector4([-1.0,1.0,1.0,1.0]), Vector4([1.0,1.0,1.0,1.0]), Vector4([1.0,1.0,-1.0,1.0]), Vector4([-1.0,1.0,-1.0,1.0])],
			[Vector4([1.0,-1.0,1.0,1.0]), Vector4([-1.0,-1.0,1.0,1.0]), Vector4([-1.0,-1.0,-1.0,1.0]), Vector4([1.0,-1.0,-1.0,1.0])]]
		self.obj_colors = [(255,0,0), (0,255,0), (0,0,255), (127,127,127), (127,0,127), (0,127,127)]

		self.fov = math.pi / 2.0

		self.cam_pos = Vector4([0.0,0.0,0.0,1.0])
		self.scr_width = scr_width
		self.scr_height = scr_height

		# initialize matrices 
		self.model = identity()
		self.projection = identity()
		self.viewport = identity()
		self.animate = animate

	def update_matrices(self):
		self.projection = projection()
		self.viewport = viewport(self.scr_width,self.scr_height,self.fov)

	# do some simple animation 
	def update_model(self,obj_pos, angle):
		tmp = rot_x(angle)*rot_y(math.pi/4.0)
		self.model = translate(obj_pos[0], obj_pos[1], obj_pos[2])*tmp

	def transform_point(self,point):
		tmp = matr_vec_mul(self.projection,point)

		# perspective divide
		tmp2 = Vector4([tmp.e[0]/tmp.e[3], tmp.e[1]/tmp.e[3],tmp.e[2]/tmp.e[3],1.0])

		tmp = matr_vec_mul(self.viewport,tmp2)
		return [tmp.e[0],tmp.e[1]]

	def transform_polygon(self,polygon):
		return [self.transform_point(point) for point in polygon]
	
	def polygon_faces_camera(self,polygon):
		v0 = polygon[0] - self.cam_pos
		v1 = polygon[1] - polygon[0]
		v2 = polygon[2] - polygon[1]

		normal = crossproduct(v1,v2)
		if (dotproduct(normal,v0) < 0.0):
			return 1
		else:
			return 0

	def run(self):
		screen = pygame.display.set_mode((self.scr_width,self.scr_height),
				pygame.RESIZABLE|pygame.DOUBLEBUF)
		angle = 0.0

		while 1:
			for event in pygame.event.get():
		  		if event.type == pygame.QUIT: sys.exit()
				if (event.type == pygame.KEYDOWN):
					# toggle animation 
					if (event.key == pygame.K_z):
						self.animate = (self.animate + 1) % 2
				# resize the window 
				if (event.type == pygame.VIDEORESIZE):
					screen = pygame.display.set_mode(event.size)
					self.scr_width = event.w
					self.scr_height = event.h

			self.update_matrices()

			if (self.animate):
				angle += 0.005
				# prevent floating point overflow 
				if (angle > 2*math.pi): 
					angle = angle - 2*math.pi 
				self.update_model([0.0,0.0,5.0],-angle)

			screen.fill((0,0,0))	

			for i in range(len(self.obj)):
				poly = self.obj[i]
				tmp = [matr_vec_mul(self.model, point) for point in poly]
				if (self.polygon_faces_camera(tmp)):
					pygame.draw.polygon(screen, self.obj_colors[i], self.transform_polygon(tmp))
			# update the screen 
			pygame.display.flip()

myapp = Application()
myapp.run()
