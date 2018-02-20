#!/usr/bin/python2


#=============================================================================#
# Name        : mazeprogram.py                                                #
# Autor       : Adrian Antonana                                               #
# Date        : July, 20 2012                                                 #
# Description : Function definitions for drawing a maze in a window using     #
#               pygame and the maze class (mymaze.py).                        #
#=============================================================================#

# imports
from maze import *
from sys import *
import pygame

#-------------------------------------------------------------------------------------#
#              function definitions for drawing the maze with pygame                  #
#-------------------------------------------------------------------------------------#

# generates a window with maze with all cells isolated from each other
def base_window(m):
  winwidth = m.cols*CELLSIZE+(m.cols+1)*WALLSIZE
  winheight = m.rows*CELLSIZE+(m.rows+1)*WALLSIZE
  w = pygame.display.set_mode((winwidth,winheight))
  w.fill(BLACK)

  for i in range(m.rows):
    for j in range(m.cols):
      pygame.draw.rect(w,WHITE,(WALLSIZE+(j*CELLSIZE+j*WALLSIZE),WALLSIZE+(i*CELLSIZE+
      i*WALLSIZE),CELLSIZE,CELLSIZE))

  return w

#--------------------------------------------------------------------------------------

# knocks down walls from base_window to create the path
def maze_window(m):
  w = base_window(m)

  for i in range(m.rows):
    for j in range(m.cols):
      if not m.maze[i][j][BOTTOMWALL]:
        pygame.draw.rect(w,WHITE,(j*CELLSIZE+(j+1)*WALLSIZE,(i+1)*CELLSIZE+(i+1)
        *WALLSIZE,CELLSIZE,WALLSIZE))
      if not m.maze[i][j][RIGHTWALL]:
        pygame.draw.rect(w,WHITE,((j+1)*CELLSIZE+(j+1)*WALLSIZE,i*CELLSIZE+(i+1)
        *WALLSIZE,WALLSIZE,CELLSIZE))

  pygame.display.update()
  return w
  
#--------------------------------------------------------------------------------------

# paints the solution path in the maze window
def maze_path_window(m,w):
  path = m.solutionpath

  # print every cell within the solution path
  for index in range(len(path)-1):
    actrow = path[index][0]
    actcol = path[index][1]
    nextrow = path[index+1][0]
    nextcol = path[index+1][1]
    pygame.draw.rect(w,RED,(actcol*CELLSIZE+(actcol+1)*WALLSIZE,actrow*CELLSIZE+(actrow+
    1)*WALLSIZE,CELLSIZE,CELLSIZE))

    # also paint the white spaces between the cells
    if actrow == nextrow:
      if actcol < nextcol:
        pygame.draw.rect(w,RED,((actcol+1)*CELLSIZE+(actcol+1)*WALLSIZE,actrow*CELLSIZE+
        (actrow+1)*WALLSIZE,WALLSIZE,CELLSIZE))
      else:
        pygame.draw.rect(w,RED,(actcol*CELLSIZE+actcol*WALLSIZE,actrow*CELLSIZE+(actrow+
        1)*WALLSIZE,WALLSIZE,CELLSIZE))
    elif actcol == nextcol:
      if actrow < nextrow:
        pygame.draw.rect(w,RED,(actcol*CELLSIZE+(actcol+1)*WALLSIZE,(actrow+1)*CELLSIZE+
        (actrow+1)*WALLSIZE,CELLSIZE,WALLSIZE))
      else:
        pygame.draw.rect(w,RED,(actcol*CELLSIZE+(actcol+1)*WALLSIZE,actrow*CELLSIZE+
        actrow*WALLSIZE,CELLSIZE,WALLSIZE))


  # add a different color for start and end cells
  startrow = path[0][0]
  startcol = path[0][1]
  endrow = path[-1][0]
  endcol = path[-1][1]

  pygame.draw.rect(w,BLUE,(startcol*CELLSIZE+(startcol+1)*WALLSIZE,startrow*CELLSIZE+(
  startrow+1)*WALLSIZE,CELLSIZE,CELLSIZE))
  pygame.draw.rect(w,GREEN,(endcol*CELLSIZE+(endcol+1)*WALLSIZE,endrow*CELLSIZE+(endrow+
  1)*WALLSIZE,CELLSIZE,CELLSIZE))
  pygame.display.update()
  

#================================================================================#
#                                Main Program                                    #
#================================================================================#

# sizes and colors
CELLSIZE = 5
WALLSIZE = 2

WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)

# get the maze size from program arguments
rows = int(argv[1])
cols = int(argv[2])

# generate random maze, solve it
maze = Maze(rows,cols)
print maze

maze.solve_maze()
#print maze
#print maze.solutionpath

# show the maze with the solution path
pygame.init()
window = maze_window(maze)
maze_path_window(maze,window)

while True:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      sys.exit()
