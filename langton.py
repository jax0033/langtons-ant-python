import pygame
import random as r
import os
#here you can decide for the rules
rules = "rl"
#initialize pygame and set window position
os.environ["SDL_VIDEO_WINDOW_POS"] = "500,35"
pygame.init()
#returns color for the rules
def get_random_color():
	return (r.randint(0,255),r.randint(0,255),r.randint(0,255))

class Board:
	def __init__(self,w,h,rules):
		#declares width height, sets all the rules as colors in list which indexes will be used as ids
		self.w = w
		self.h = h
		self.rules = rules
		self.color = [get_random_color() for n in range(len(rules))]
		self.running = False
		#ant position in the middle of the board
		self.ant = [w//2,h//2]
		#declares movement information for the ant
		self.index = 0
		self.orientation = 0
		self.or_index = [[-1,0],[0,-1],[1,0],[0,1]]
		self.length = len(rules)-1
		self.screen = pygame.display.set_mode((self.w,self.h))

	#adds values of same size lists
	def add(self,a,b):
		a[0] = a[0]+b[0]
		a[1] = a[1]+b[1]
		return a

	
	def move_right(self):
		#choses next available color
		if self.index+1 > self.length:
			self.index = 0
		else:
			self.index += 1

		self.draw(self.ant[0],self.ant[1],self.color[self.index])

		#changes movement vector of the ant
		self.orientation += 1
		if self.orientation > 3:
			self.orientation = 0
		self.ant = self.add(self.ant,self.or_index[self.orientation])

	
	def move_left(self):
		#choses next available color

		if self.index+1 > self.length:
			self.index = 0
		else:
			self.index += 1

		self.draw(self.ant[0],self.ant[1],self.color[self.index])

		self.orientation -= 1
		if self.orientation < 0:
			self.orientation = 3

		self.ant = self.add(self.ant,self.or_index[self.orientation])

	
	def format(self):
		#checks if the ant goes right or left
		if self.rules[self.index] == "r":
			self.move_right()
			return
		if self.rules[self.index] == "l":
			self.move_left()
			return

	
	def iterate(self):
		#gets the color of the field the ant is standing on
		ANT_POS = self.screen.get_at(self.ant)
		ANT_POS = ANT_POS[0],ANT_POS[1],ANT_POS[2]
		#checks in colors for the color to get the index / id of the color
		for ind,color_id in enumerate(self.color):
			if ANT_POS == color_id:

				self.index = ind
				self.format()
				return

	
	def draw(self,x,y,color):
		self.screen.set_at((x,y),color)

	
	def run (self):
		#fills the screen with the first color so the ant can begin moving
		self.screen.fill(self.color[0])
		self.running = True
		while self.running:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					quit()
			self.iterate()
			pygame.display.update()

if __name__ == "__main__":
	#window size and rules
	b = Board(1000,1000,rules)
	b.run()
