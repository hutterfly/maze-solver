import time 
import tkinter as tk
import maze_gen
import search

cell_size = 20
complexity = 10
maze_gen.changeMazeComplexity(complexity)
maze, startPoint, endPoint = maze_gen.prim()
graph = {}
search.addAllEdgesFromMaze(graph, maze)

dfspath, bfspath, astarmanhatpath, astareuclidpath = [], [], [], []
dfsvisited, bfsvisited, astarmanhatvisited, astareuclidvisited = [], [], [], []
dfsRunTime, bfsRunTime, astarManHatRunTime, astarEuclidRunTime = 0, 0, 0, 0

def draw_maze(maze, cell_size):
    for col in range(maze.shape[0]):
        for row in range(maze.shape[1]):
            if maze[col][row] == 1:
                x1 = row * cell_size
                y1 = col * cell_size
                x2 = x1 + cell_size
                y2 = y1 + cell_size
                canvas.create_rectangle(x1, y1, x2, y2, fill="black", outline="black")

def draw_start_end(startPoint, endPoint, cell_size):
    x1 = startPoint[1] * cell_size
    y1 = startPoint[0] * cell_size
    x2 = x1 + cell_size
    y2 = y1 + cell_size
    canvas.create_rectangle(x1, y1, x2, y2, fill="red", outline="red")
    x3 = endPoint[1] * cell_size
    y3 = endPoint[0] * cell_size
    x4 = x3 + cell_size
    y4 = y3 + cell_size
    canvas.create_rectangle(x3, y3, x4, y4, fill="green", outline="green")

def draw_new_maze():
    global cell_size, complexity
    canvas.delete("all")
    create_new_maze(complexity)
    draw_maze(maze, cell_size)
    draw_start_end(startPoint, endPoint, cell_size)
    clear_labels()

def create_new_maze(complexity=10):
    global maze, startPoint, endPoint, graph
    maze_gen.changeMazeComplexity(complexity)
    maze, startPoint, endPoint = maze_gen.prim()
    graph = {}
    search.addAllEdgesFromMaze(graph, maze)

def draw_path(path, cell_size, color="blue", delay=50, step=0):
    if step != len(path):
        x1 = path[step][1] * cell_size
        y1 = path[step][0] * cell_size
        x2 = x1 + cell_size
        y2 = y1 + cell_size
        cell = canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline=color)
        killCell = (len(path) - step) * delay
        root.after(killCell, lambda : delete_cell(cell))
        root.after(delay, lambda : draw_path(path, cell_size, color, delay, step + 1))

def clear_labels():
    dfsRunTimeLabel.config(text="dfsRunTime: 0")
    dfsPathLengthLabel.config(text="dfsPathLength: 0")
    dfsNodesVisitedLabel.config(text="dfsNodesVisited: 0")
    bfsRunTimeLabel.config(text="bfsRunTime: 0")
    bfsPathLengthLabel.config(text="bfsPathLength: 0")
    bfsNodesVisitedLabel.config(text="bfsNodesVisited: 0")
    astarManHatRunTimeLabel.config(text="A*MHRunTime: 0" )
    astarManHatPathLengthLabel.config(text="A*MHPathLength: 0")
    astarManHatNodesVisitedLabel.config(text="A*MHNodesVisited: 0")
    astarEuclidRunTimeLabel.config(text="A*ERunTime: 0")
    astarEuclidPathLengthLabel.config(text="A*EPathLength: 0")
    astarEuclidNodesVisitedLabel.config(text="A*ENodesVisited: 0")

def dfs():
    global dfspath, dfsvisited, dfsRunTime, cell_size, graph, startPoint, endPoint
    dfsStartTime = time.time()
    dfspath, dfsvisited = search.dfs(graph, startPoint, endPoint)
    dfsRunTime = time.time() - dfsStartTime

    dfsRunTimeLabel.config(text="dfsRunTime: " + str(dfsRunTime))
    dfsPathLengthLabel.config(text="dfsPathLength: " + str(len(dfspath)))
    dfsNodesVisitedLabel.config(text="dfsNodesVisited: " + str(len(dfsvisited)))

    draw_path(dfsvisited, cell_size, "yellow")
    pathDelay = len(dfsvisited) * 50
    root.after(pathDelay, lambda : draw_path(dfspath, cell_size))

def bfs():
    global bfspath, bfsvisited, bfsRunTime, cell_size, graph, startPoint, endPoint
    bfsStartTime = time.time()
    bfspath, bfsvisited = search.bfs(graph, startPoint, endPoint)
    bfsRunTime = time.time() - bfsStartTime

    bfsRunTimeLabel.config(text="bfsRunTime: " + str(bfsRunTime))
    bfsPathLengthLabel.config(text="bfsPathLength: " + str(len(bfspath)))
    bfsNodesVisitedLabel.config(text="bfsNodesVisited: " + str(len(bfsvisited)))

    draw_path(bfsvisited, cell_size, "yellow")
    pathDelay = len(bfsvisited) * 50
    root.after(pathDelay, lambda : draw_path(bfspath, cell_size))

def astar_manhat():
    global astarmanhatpath, astarmanhatvisited, astarManHatRunTime, cell_size, graph, startPoint, endPoint
    astarStartTime = time.time()
    astarmanhatpath, astarmanhatvisited = search.aStar(graph, startPoint, endPoint, True)
    astarManHatRunTime = time.time() - astarStartTime

    astarManHatRunTimeLabel.config(text="A*MHRunTime: " + str(astarManHatRunTime))
    astarManHatPathLengthLabel.config(text="A*MHPathLength: " + str(len(astarmanhatpath)))
    astarManHatNodesVisitedLabel.config(text="A*MHNodesVisited: " + str(len(astarmanhatvisited)))

    draw_path(astarmanhatvisited, cell_size, "yellow")
    pathDelay = len(astarmanhatvisited) * 50
    root.after(pathDelay, lambda : draw_path(astarmanhatpath, cell_size))

def astar_euclid():
    global astareuclidpath, astareuclidvisited, astarEuclidRunTime, cell_size, graph, startPoint, endPoint
    astarStartTime = time.time()
    astareuclidpath, astareuclidvisited = search.aStar(graph, startPoint, endPoint, False)
    astarEuclidRunTime = time.time() - astarStartTime

    astarEuclidRunTimeLabel.config(text="A*ERunTime: " + str(astarEuclidRunTime))
    astarEuclidPathLengthLabel.config(text="A*EPathLength: " + str(len(astareuclidpath)))
    astarEuclidNodesVisitedLabel.config(text="A*ENodesVisited: " + str(len(astareuclidvisited)))

    draw_path(astareuclidvisited, cell_size, "yellow")
    pathDelay = len(astareuclidvisited) * 50
    root.after(pathDelay, lambda : draw_path(astareuclidpath, cell_size))

def delete_cell(cell):
    canvas.delete(cell)

root = tk.Tk()
root.title("visualization of pathfinding algorithms")
canvas = tk.Canvas(root, width=maze.shape[1] * cell_size, height=maze.shape[0] * cell_size)
canvas.pack()
draw_maze(maze, cell_size)
draw_start_end(startPoint, endPoint, cell_size)

dfsFrame = tk.Frame(root)
dfsFrame.pack(padx=5, pady=5)
dfsbtn = tk.Button(dfsFrame, text="dfs", command=dfs)
dfsbtn.pack(side="left")
dfsRunTimeLabel = tk.Label(dfsFrame, text="dfsRunTime: " + str(dfsRunTime))
dfsRunTimeLabel.pack(side="right")
dfsPathLengthLabel = tk.Label(dfsFrame, text="dfsPathLength: " + str(len(dfspath)))
dfsPathLengthLabel.pack(side="right")
dfsNodesVisitedLabel = tk.Label(dfsFrame, text="dfsNodesVisited: " + str(len(dfsvisited)))
dfsNodesVisitedLabel.pack(side="right")

bfsFrame = tk.Frame(root)
bfsFrame.pack(padx=5, pady=5)
bfsbtn = tk.Button(bfsFrame, text="bfs", command=bfs)
bfsbtn.pack(side="left")
bfsRunTimeLabel = tk.Label(bfsFrame, text="bfsRunTime: 0")
bfsRunTimeLabel.pack(side="right")
bfsPathLengthLabel = tk.Label(bfsFrame, text="bfsPathLength: 0")
bfsPathLengthLabel.pack(side="right")
bfsNodesVisitedLabel = tk.Label(bfsFrame, text="bfsNodesVisited: 0")
bfsNodesVisitedLabel.pack(side="right")

astarManHatFrame = tk.Frame(root)
astarManHatFrame.pack(padx=5, pady=5)
astarManHatbtn = tk.Button(astarManHatFrame, text="A*MH", command=astar_manhat)
astarManHatbtn.pack(side="left")
astarManHatRunTimeLabel = tk.Label(astarManHatFrame, text="A*MHRunTime: 0")
astarManHatRunTimeLabel.pack(side="right")
astarManHatPathLengthLabel = tk.Label(astarManHatFrame, text="A*MHPathLength: 0")
astarManHatPathLengthLabel.pack(side="right")
astarManHatNodesVisitedLabel = tk.Label(astarManHatFrame, text="A*MHNodesVisited: 0")
astarManHatNodesVisitedLabel.pack(side="right")

astarEuclidFrame = tk.Frame(root)
astarEuclidFrame.pack(padx=5, pady=5)
astarEuclidtbtn = tk.Button(astarEuclidFrame, text="A*E", command=astar_euclid)
astarEuclidtbtn.pack(side="left")
astarEuclidRunTimeLabel = tk.Label(astarEuclidFrame, text="A*ERunTime: 0")
astarEuclidRunTimeLabel.pack(side="right")
astarEuclidPathLengthLabel = tk.Label(astarEuclidFrame, text="A*EPathLength: 0")
astarEuclidPathLengthLabel.pack(side="right")
astarEuclidNodesVisitedLabel = tk.Label(astarEuclidFrame, text="A*ENodesVisited: 0")
astarEuclidNodesVisitedLabel.pack(side="right")

newMazeFrame = tk.Frame(root)
newMazeFrame.pack(padx=5, pady=5)
newMazeBtn = tk.Button(newMazeFrame, text="newMaze", command=draw_new_maze)
newMazeBtn.pack()

root.mainloop()