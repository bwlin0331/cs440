# Generates 2x2 matrix for maze using DFS random tiebreaking

import random
import sys
import math
import pygame
import heapq

dx = [0, 1, 0, -1]; dy = [-1, 0, 1, 0]
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
# This sets the WIDTH and HEIGHT of each grid location
WIDTH =	8
HEIGHT = 8
 
# This sets the margin between each cell
MARGIN = 1

openSet = []
closedSet = {}
counter = 0


class node():
	def __init__(self, point, parent, g, h):
		self.point = point
		self.parent = parent
		self.g = g
		self.h = h

	def getf():
		return self.g + self.h


def randomPoint(x,y):
	return (random.randint(0,x-1),random.randint(0,y-1))

	

def pointEquals(a,b):
	if ( a[0] == b[0] and a[1] == b[1] ):
		return 1
	else:
		return 0

def heuristic_func(start,goal):
    return abs(start[0]-goal[0]) + abs(start[1]-goal[1])

#def dfstie(maze):

class Maze(object):
	def __init__(self, x= 101, y=101):
		self.x = x
		self.y = y
		self.maze = [[0 for i in range(self.x)] for j in range(self.y)]
		self.start = node(None,None,None,None)
		self.goal = node(None,None,None,None)
	
	#def dfsMaze():

def generateMaze(m):
	temp = randomPoint(m.x,m.y)
	stack = [temp]
	visited_set = set()
	visited_set.add(((temp[0],temp[1])))
	while len(stack) > 0:
	    (cx, cy) = stack[-1]
	    visited_set.add((cx, cy))	
	    if random.random() < .30:
	    	m.maze[cx][cy] = 0
	    else: 
	    	m.maze[cx][cy] = 1

	    # find a new cell to add
	    nlst = [] # list of available neighbors
	    for i in range(4):
	        nx = cx + dx[i]; ny = cy + dy[i]
	        if nx >= 0 and nx < m.x and ny >= 0 and ny < m.y:
	            if (nx,ny) not in visited_set:
	                # of occupied neighbors must be 1
	                nlst.append(i)
	    # if 1 or more neighbors available then randomly select one and move
	    if len(nlst) > 0:
	        ir = nlst[random.randint(0, len(nlst) - 1)]
	        cx += dx[ir]; cy += dy[ir]
	        stack.append((cx, cy))
	    else: stack.pop()
	


def computePath(start, goal):
	
	# Set of nodes to be evaluated
	return 0
	


mx = 101

my = 101
maze = Maze(mx,my)




#omaze = [[1 for i in range(maze.x)] for j in range(maze.y)]
#print('\n'.join([''.join(['{:4}'.format(item) for item in row]) for row in maze.maze]))
for i in range (1,51):
	generateMaze(maze)
	f = open('testcases/testcase'+str(i),'w')
	f.write('[{}]'.format(',\n'.join(['[{}]'.format(','.join(['{}'.format(item) for item in row])) for row in maze.maze])))
	f.close()

#print('\n')
#print('[{}]'.format(',\n'.join(['[{}]'.format(','.join(['{}'.format(item) for item in row])) for row in maze.maze])))
maze.start.point = randomPoint(mx,my)
maze.maze[maze.start.point[0]][maze.start.point[1]] = 1


maze.goal.point = randomPoint(mx,my)
while(pointEquals(maze.start.point,maze.goal.point)):
		maze.goal.point = randomPoint(mx,my)
maze.maze[maze.goal.point[0]][maze.goal.point[1]] = 1


#print(pointString(maze.start) + "\n" + pointString(maze.goal))
# pygame.init()
# size =((WIDTH+MARGIN)*maze.y,(WIDTH+HEIGHT)*maze.x)
# sq_size = 64
# screen = pygame.display.set_mode(size)
# pygame.display.set_caption("A*")
# done = False 
# clock = pygame.time.Clock()
# #Main program loop
# while not done:
# 	for event in pygame.event.get():  # User did something
# 		if event.type == pygame.QUIT:  # If user clicked close
# 			done = True  # Flag that we are done so we exit this loop
# 			#elif event.type == pygame.MOUSEBUTTONDOWN:

# 	# Set the screen background
# 	screen.fill(BLACK)
# 	for row in range(maze.x):
# 		for column in range(maze.y):
# 			color = BLACK
# 			if maze.maze[row][column] == 1:
# 				color = WHITE
# 			if maze.start.point[0] == row and maze.start.point[1] == column:
# 				color = GREEN
# 			if maze.goal.point[0] == row and maze.goal.point[1] == column:
# 				color = RED
# 			pygame.draw.rect(screen,color,
# 			[(MARGIN + WIDTH) * column + MARGIN, 
# 			(MARGIN + HEIGHT) * row + MARGIN,
# 			WIDTH,
# 			HEIGHT])

# 	# Limit to 60 frames per second
# 	clock.tick(60)
# 	pygame.display.flip()

# pygame.quit()