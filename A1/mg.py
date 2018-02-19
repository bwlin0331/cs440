# Generates 2x2 matrix for maze using DFS random tiebreaking

import random
import sys
import math
import pygame

dx = [0, 1, 0, -1]; dy = [-1, 0, 1, 0]
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
# This sets the WIDTH and HEIGHT of each grid location
WIDTH = 20
HEIGHT = 20
 
# This sets the margin between each cell
MARGIN = 5

class Point(object):

	def __init__(self, x=0, y=0):
		self.x = x
		self.y = y

		
	@staticmethod
	def randomPoint(x,y):
		return Point(random.randint(0,x-1),random.randint(0,y-1))

	

def pointEquals(a,b):
	if ( a.x == b.x and a.y == b.y ):
		return 1
	else:
		return 0

def pointString(a):
	return str(a.x) + "," + str(a.y)

#def dfstie(maze):

class Maze(object):
	def __init__(self, x= 101, y=101):
		self.x = x
		self.y = y
		self.maze = [[0 for i in range(self.x)] for j in range(self.y)]
		self.start = Point()
		self.goal = Point()

	
	#def dfsMaze():

def generateMaze(m):
	m.start = Point.randomPoint(m.x,m.y)
	temp = Point.randomPoint(m.x,m.y)
	stack = [(m.start.x,m.start.y)]
	while len(stack) > 0:
	    (cx, cy) = stack[-1]
	    m.maze[cy][cx] = 1
	    # find a new cell to add
	    nlst = [] # list of available neighbors
	    for i in range(4):
	        nx = cx + dx[i]; ny = cy + dy[i]
	        if nx >= 0 and nx < m.x and ny >= 0 and ny < m.y:
	            if m.maze[ny][nx] == 0:
	                # of occupied neighbors must be 1
	                ctr = 0
	                for j in range(4):
	                    ex = nx + dx[j]; ey = ny + dy[j]
	                    if ex >= 0 and ex < m.x and ey >= 0 and ey < m.y:
	                        if m.maze[ey][ex] == 1: ctr += 1
	                if ctr == 1: nlst.append(i)
	    # if 1 or more neighbors available then randomly select one and move
	    if len(nlst) > 0:
	        ir = nlst[random.randint(0, len(nlst) - 1)]
	        cx += dx[ir]; cy += dy[ir]
	        stack.append((cx, cy))
	    else: stack.pop()
	while(pointEquals(m.start,temp) or m.maze[temp.x][temp.y] == 0):
		temp = Point.randomPoint(m.x,m.y)
		#print(pointString(temp) + "\n")
	else:
		m.goal = temp



if len(sys.argv) > 1:
	mx = int(sys.argv[1])
	my = int(sys.argv[2])
else:
	mx = 101
	my = 101

maze = Maze(mx,my)
#print('\n'.join([''.join(['{:4}'.format(item) for item in row]) for row in maze.maze]))
generateMaze(maze)
#print('\n')
print('\n'.join([''.join(['{:4}'.format(item) for item in row]) for row in maze.maze]))

#print(pointString(maze.start) + "\n" + pointString(maze.goal))
pygame.init()
size =(1024,1024)
sq_size = 64
screen = pygame.display.set_mode(size)
pygame.display.set_caption("A*")
done = False 
clock = pygame.time.Clock()
while not done:
	for event in pygame.event.get():  # User did something
	    if event.type == pygame.QUIT:  # If user clicked close
	        done = True  # Flag that we are done so we exit this loop
	    elif event.type == pygame.MOUSEBUTTONDOWN:
	       
	        print("Click ", pos, "Grid coordinates: ", row, column)
	    # Set the screen background
	screen.fill(BLACK)
	for row in range(maze.x):
		for column in range(maze.y):
       			color = BLACK
           	if maze.maze[row][column] == 1:
       		    color = WHITE
          	pygame.draw.rect(screen,color,
          		[(MARGIN + WIDTH) * column + MARGIN, 
          		(MARGIN + HEIGHT) * row + MARGIN,
          		WIDTH,
          		HEIGHT])
 
    # Limit to 60 frames per second
   	clock.tick(60)

   	pygame.display.flip()

pygame.quit()