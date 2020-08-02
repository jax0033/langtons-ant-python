import pygame
import random
import os

randcolors = [(random.randint(0,255),random.randint(0,255),random.randint(0,255)) for i in range(33)]

os.environ["SDL_VIDEO_WINDOW_POS"] = "700,35"
pygame.init()
width,heigth = 1000,1000
screen = pygame.display.set_mode((width,heigth))

class Board:

	class Cursor:
		def __init__(self,board):
			board = board
			self.pos = [len(board)//2, 
						len(board[0])//2]
			self.directions = ("up","right","down","left")
			self.direction = 3

		def move_right(self):
			if self.direction == 3:
				self.direction = 0
			else: 
				self.direction += 1
			self.move()

		def move_left(self):
			if self.direction == 0:
				self.direction = 3
			else:
				self.direction -= 1
			self.move()

		def move(self):
			if self.direction == 0:
				self.pos = [self.pos[0],self.pos[1]-1]
			elif self.direction == 1:
				self.pos = [self.pos[0]+1,self.pos[1]]
			elif self.direction == 2:
				self.pos = [self.pos[0],self.pos[1]+1]
			elif self.direction == 3:
				self.pos = [self.pos[0]-1,self.pos[1]]

	def __init__(self):
		self.board = [[0 for i in range(1000)] for i in range(1000)]
		self.cursor = self.Cursor(self.board)
		#self.squares = [(0, 0,  (255,255,255)),
		#				(1, 1,  (0,0,0)), 
		#				(2, 0,  (34,178,255)),
		#				(3, 1,  (81,163,31)),
		#				(4,)]
		self.squares = [(n,0,randcolors[n]) for n in range(len("RLLLLLRRL"))]
#RLLLLLRRL
	def act(self):
		tile_id = self.board[self.cursor.pos[0]][self.cursor.pos[1]] 
		if tile_id == 0:
			self.board[self.cursor.pos[0]][self.cursor.pos[1]] = 1
			self.draw(self.cursor.pos[0],self.cursor.pos[1],self.squares[1][2])
			self.cursor.move_right()
		
		elif tile_id == 1:
			self.board[self.cursor.pos[0]][self.cursor.pos[1]] = 2
			self.draw(self.cursor.pos[0],self.cursor.pos[1],self.squares[2][2])
			self.cursor.move_left()
		
		elif tile_id == 2:
			self.board[self.cursor.pos[0]][self.cursor.pos[1]] = 3
			self.draw(self.cursor.pos[0],self.cursor.pos[1],self.squares[3][2])
			self.cursor.move_left()

		elif tile_id == 3:
			self.board[self.cursor.pos[0]][self.cursor.pos[1]] = 4
			self.draw(self.cursor.pos[0],self.cursor.pos[1],self.squares[4][2])
			self.cursor.move_left()
		
		elif tile_id == 4:
			self.board[self.cursor.pos[0]][self.cursor.pos[1]] = 5
			self.draw(self.cursor.pos[0],self.cursor.pos[1],self.squares[5][2])
			self.cursor.move_left()

		elif tile_id == 5:
			self.board[self.cursor.pos[0]][self.cursor.pos[1]] = 6
			self.draw(self.cursor.pos[0],self.cursor.pos[1],self.squares[6][2])
			self.cursor.move_left()
		
		elif tile_id == 6:
			self.board[self.cursor.pos[0]][self.cursor.pos[1]] = 7
			self.draw(self.cursor.pos[0],self.cursor.pos[1],self.squares[7][2])
			self.cursor.move_right()

		elif tile_id == 7:
			self.board[self.cursor.pos[0]][self.cursor.pos[1]] = 8
			self.draw(self.cursor.pos[0],self.cursor.pos[1],self.squares[8][2])
			self.cursor.move_right()
		
		elif tile_id == 8:
			self.board[self.cursor.pos[0]][self.cursor.pos[1]] = 0
			self.draw(self.cursor.pos[0],self.cursor.pos[1],self.squares[0][2])
			self.cursor.move_left()
	
	def draw(self,x,y,color):
		pygame.draw.rect(screen,color,pygame.Rect(x*1,y*1,1,1))

def main():
	fps = 500
	clock = pygame.time.Clock()
	running = True
	board = Board()
	screen.fill((255,255,255))
	pygame.display.update()
	while running:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()

		board.act()

		pygame.display.update()
		#clock.tick(fps)


main()