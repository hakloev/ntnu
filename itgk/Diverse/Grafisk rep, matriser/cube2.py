# This program is free software. It comes without any warranty, 
# to the extent permitted by applicable law. You can redistribute 
# it and/or modify it under the terms of the Do What The Fuck You 
# Want To Public License, Version 2, as published by Sam Hocevar. 
# See http://sam.zoy.org/wtfpl/COPYING for more details. 

import sys,math,pygame,copy

from linalg4 import *

# removes the part of the polygon that is behind the plane
# need this for the application to function properly, but the math here is 
# not relevant to the course MA0003
def clip_polygon(polygon, plane_normal, plane_dist):
	result = []
	for i in range(len(polygon)):
		cur = polygon[i]
		next = polygon[(i+1) % len(polygon)]
		cur_dist = dotproduct(plane_normal,cur) - plane_dist
		next_dist = dotproduct(plane_normal,next) - plane_dist
		cur_in = (cur_dist > 0.0)
		next_in = (next_dist > 0.0) 

		if cur_in:
			result.append(cur)

		if (cur_in != next_in):
			scale = cur_dist/(cur_dist - next_dist)
			newpoint = cur + scale*(next-cur)
			result.append(newpoint)
	return result

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

		self.rot_x = 0.0
		self.rot_y = 0.0
		self.rot_z = 0.0
		self.fov = math.pi / 2.0
		self.frustum = []

		self.cam_pos = Vector4([0.0,0.0,-3.0,1.0])
		self.scr_width = scr_width
		self.scr_height = scr_height

		# initialize matrices 
		self.model = identity()
		self.view = identity()
		self.view_inv = identity()
		self.projection = identity()
		self.viewport = identity()
		self.animate = animate

	def update_matrices(self):
		self.projection = projection()
		self.viewport = viewport(self.scr_width,self.scr_height,self.fov)

		tmp = rot_x(self.rot_x)*rot_z(self.rot_z)*rot_y(self.rot_y)
		self.view = tmp*translate(-self.cam_pos.e[0],-self.cam_pos.e[1], -self.cam_pos.e[2])

		tmp = rot_y(-self.rot_y)*rot_z(-self.rot_z)*rot_x(-self.rot_x)
		self.view_inv = translate(self.cam_pos.e[0],self.cam_pos.e[1],self.cam_pos.e[2])*tmp

	def update_model(self,obj_pos, angle):	
		tmp = rot_x(angle)*rot_y(math.pi/4.0)
		self.model = translate(obj_pos[0], obj_pos[1], obj_pos[2])*tmp

	def transform_point(self,point):
		tmp = matr_vec_mul(self.projection*self.view,point)

		# perspective divide
		tmp2 = Vector4([tmp.e[0]/tmp.e[3], tmp.e[1]/tmp.e[3],tmp.e[2]/tmp.e[3],1.0])

		tmp = matr_vec_mul(self.viewport,tmp2)
		return [tmp.e[0],tmp.e[1]]

	def transform_polygon(self,polygon):
		return [self.transform_point(point) for point in polygon]
	
	# set up the view-volume (geometrically, it's an infinite pyramid with apex at the camera position)
	def set_up_frustum(self):
		self.frustum = []
		s = math.sin(self.fov/2.0)
		c = math.cos(self.fov/2.0)

		aspect_ratio = float(self.scr_width)/float(self.scr_height)

		left = Vector4([-c,0.0,s,0.0])
		right = Vector4([c,0.0,s,0.0])

		angle = math.atan(math.tan(self.fov/2.0)*aspect_ratio)
		s = math.sin(angle)
		c = math.cos(angle)
		top = Vector4([0.0, -c, s, 0.0])
		bottom = Vector4([0.0, c, s, 0.0])

		self.frustum.append([matr_vec_mul(self.view_inv,left), dotproduct(matr_vec_mul(self.view_inv,left),self.cam_pos)])
		self.frustum.append([matr_vec_mul(self.view_inv,right), dotproduct(matr_vec_mul(self.view_inv,right), self.cam_pos)])
		self.frustum.append([matr_vec_mul(self.view_inv,top), dotproduct(matr_vec_mul(self.view_inv,top), self.cam_pos)])
		self.frustum.append([matr_vec_mul(self.view_inv,bottom), dotproduct(matr_vec_mul(self.view_inv,bottom), self.cam_pos)])

	# throw away bits of object(s) that are outside the view-volume
	def clip_to_frustum(self, polygon):
		# make a copy
		tmp = [Vector4([polygon[j].e[i] for i in range(len(polygon[j].e))]) for j in range(len(polygon))]

		for plane in self.frustum:
			tmp = clip_polygon(tmp,plane[0],plane[1])
		return tmp
	
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
				if (event.type == pygame.VIDEORESIZE):
						screen = pygame.display.set_mode(event.size)
						self.scr_width = event.w
						self.scr_height = event.h

			# for movement (could also have just picked out first, second 
			# and third column of the inverse view matrix (self.view_inv) directly)

			forward = matr_vec_mul(self.view_inv, Vector4([0.0,0.0,1.0,0.0]))
			up = matr_vec_mul(self.view_inv, Vector4([0.0,1.0,0.0,0.0]))
			right = matr_vec_mul(self.view_inv, Vector4([1.0,0.0,0.0,0.0]))

			# make stuff happen based on which keys the user presses
			keyboard_state = pygame.key.get_pressed()
			if (keyboard_state[pygame.K_LEFT]): 
				self.rot_y += 0.01
			if (keyboard_state[pygame.K_RIGHT]):
		 		self.rot_y -= 0.01
			if (keyboard_state[pygame.K_ESCAPE]):
				sys.exit()
			if (keyboard_state[pygame.K_PAGEUP]):
				self.rot_x += 0.01
			if (keyboard_state[pygame.K_PAGEDOWN]):
				self.rot_x -= 0.01
			if (keyboard_state[pygame.K_n]):
				self.rot_z += 0.01
			if (keyboard_state[pygame.K_m]):
				self.rot_z -= 0.01
			if (keyboard_state[pygame.K_HOME]):
				self.fov += 0.01
			if (keyboard_state[pygame.K_END]):
				self.fov -= 0.01

		        if (keyboard_state[pygame.K_w]):
				self.cam_pos = self.cam_pos + 0.03*forward
		        if (keyboard_state[pygame.K_s]):
				self.cam_pos = self.cam_pos - 0.03*forward
			if (keyboard_state[pygame.K_a]):
				self.cam_pos = self.cam_pos - 0.03*right
			if (keyboard_state[pygame.K_d]):
				self.cam_pos = self.cam_pos + 0.03*right
			if (keyboard_state[pygame.K_e]):
				self.cam_pos = self.cam_pos + 0.03*up
			if (keyboard_state[pygame.K_c]):
				self.cam_pos = self.cam_pos - 0.03*up

			self.update_matrices()	

			if (self.animate):
				angle += 0.01
				# prevent floating point overflow 
				if (angle > 2*math.pi): 
					angle = angle - 2*math.pi 
				self.update_model([0.0,0.0,1.0],-angle)

			self.set_up_frustum()

			screen.fill((0,0,0))	

			for i in range(len(self.obj)):
				poly = self.obj[i]
				tmp = [matr_vec_mul(self.model, point) for point in poly]
				if (self.polygon_faces_camera(tmp)):
					tmp = self.clip_to_frustum(tmp)
					# if something is still left of the polygon, draw it 
					if (len(tmp) > 2):
						pygame.draw.polygon(screen, self.obj_colors[i], self.transform_polygon(tmp))

			pygame.display.flip()

myapp = Application()
myapp.run()