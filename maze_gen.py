import numpy as np
import random

#ones represent walls
maze = np.ones((8, 12)) #default complexity is 4
wall_list = []

def changeMazeComplexity(complexity): 
    global maze
    maze = np.ones((2 * complexity, 3 * complexity))

def getRandCell():
    return (random.randint(0, maze.shape[0] - 1), random.randint(0, maze.shape[1] - 1))

def addWallsToWallList(cell): #(y, x)
    maze[cell] = 0 #make cell part of maze
    above = (cell[0] - 1, cell[1])
    below = (cell[0] + 1, cell[1])
    right = (cell[0], cell[1] + 1)
    left = (cell[0], cell[1] - 1)
    #check if cell's neighbors are within bounds, check if they are walls, and if they are walls add them to wall_list
    if above[0] > -1:
        if maze[above] == 1:
            wall_list.append(above)
    if below[0] < maze.shape[0]:
        if maze[below] == 1:
            wall_list.append(below)
    if right[1] < maze.shape[1]:
        if maze[right] == 1:
            wall_list.append(right)
    if left[1] > -1:
        if maze[left] == 1:
            wall_list.append(left)

def checkWall(cell): #will return true if only one neighbor is part of maze, and will return false otherwise
    above = (cell[0] - 1, cell[1])
    below = (cell[0] + 1, cell[1])
    right = (cell[0], cell[1] + 1)
    left = (cell[0], cell[1] - 1)
    counter = 0 #keep track of how many of the cell's neighbors are part of the maze
    if above[0] > -1:
        if maze[above] == 0:
            counter += 1
    if below[0] < maze.shape[0]:
        if maze[below] == 0:
            counter += 1
    if right[1] < maze.shape[1]:
        if maze[right] == 0:
            counter += 1
    if left[1] > -1:
        if maze[left] == 0:
            counter += 1
    if counter == 1:
        return True
    return False

def prim():
    global maze
    randCell = getRandCell()
    addWallsToWallList(randCell)

    while len(wall_list) != 0:
        randWall = random.randint(0, len(wall_list) - 1)
        if checkWall(wall_list[randWall]):
            maze[wall_list[randWall]] = 0
            addWallsToWallList(wall_list[randWall])
        wall_list.pop(randWall)

    edge = np.zeros((maze.shape[0], 1))
    maze = np.concatenate((edge, maze, edge), axis=1)

    startPoint = (random.randint(0, maze.shape[0] - 1), 0) #random point along the left most side
    endPoint = (random.randint(0, maze.shape[0] - 1), maze.shape[1] - 1) #random point along the right most side

    return maze, startPoint, endPoint