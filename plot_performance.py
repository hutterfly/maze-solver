import maze_gen
import search
import time
import matplotlib.pyplot as plt

dfsPathLength, bfsPathLength, astarManHatPathLength, astarEuclidPathLength = [], [], [], []
dfsVisitedNum, bfsVisitedNum, astarManHatVisitedNum, astarEuclidVisitedNum = [], [], [], []
dfsRunTimeNum, bfsRunTimeNum, astarManHatRunTimeNum, astarEuclidRunTimeNum = [], [], [], []

def benchmark_all():
    for i in range(1, 21):
        maze_gen.changeMazeComplexity(i)
        maze, startPoint, endPoint = maze_gen.prim()
        graph = {}
        search.addAllEdgesFromMaze(graph, maze)
        benchmark_dfs(graph, startPoint, endPoint)
        benchmark_bfs(graph, startPoint, endPoint)
        benchmark_astarmanhat(graph, startPoint, endPoint)
        benchmark_astareuclid(graph, startPoint, endPoint)

def benchmark_dfs(graph, startPoint, endPoint):
    global dfsPathLength, dfsVisitedNum, dfsRunTimeNum
    dfsStartTime = time.time()
    dfspath, dfsvisited = search.dfs(graph, startPoint, endPoint)
    dfsRunTime = time.time() - dfsStartTime
    dfsPathLength.append(len(dfspath))
    dfsVisitedNum.append(len(dfsvisited))
    dfsRunTimeNum.append(dfsRunTime)        


def benchmark_bfs(graph, startPoint, endPoint):
    global bfsPathLength, bfsVisitedNum, bfsRunTimeNum
    bfsStartTime = time.time()
    bfspath, bfsvisited = search.bfs(graph, startPoint, endPoint)
    bfsRunTime = time.time() - bfsStartTime
    bfsPathLength.append(len(bfspath))
    bfsVisitedNum.append(len(bfsvisited))
    bfsRunTimeNum.append(bfsRunTime)

def benchmark_astarmanhat(graph, startPoint, endPoint):
    global astarManHatPathLength, astarManHatVisitedNum, astarManHatRunTimeNum
    astarStartTime = time.time()
    astarmanhatpath, astarmanhatvisited = search.aStar(graph, startPoint, endPoint, True)
    astarManHatRunTime = time.time() - astarStartTime
    astarManHatPathLength.append(len(astarmanhatpath))
    astarManHatVisitedNum.append(len(astarmanhatvisited))
    astarManHatRunTimeNum.append(astarManHatRunTime)

def benchmark_astareuclid(graph, startPoint, endPoint):
    global astarEuclidPathLength, astarEuclidVisitedNum, astarEuclidRunTimeNum
    astarStartTime = time.time()
    astareuclidpath, astareuclidvisited = search.aStar(graph, startPoint, endPoint, False)
    astarEuclidRunTime = time.time() - astarStartTime
    astarEuclidPathLength.append(len(astareuclidpath))
    astarEuclidVisitedNum.append(len(astareuclidvisited))
    astarEuclidRunTimeNum.append(astarEuclidRunTime)
    


benchmark_all()
x_axis = list(range(1, 21))

plt.subplot(3, 1, 1)
plt.plot(x_axis, dfsPathLength, label = "dfs")
plt.plot(x_axis, bfsPathLength, label = "bfs", ls='dashed')
plt.plot(x_axis, astarManHatPathLength, label = "A*MH", ls='dashdot')
plt.plot(x_axis, astarEuclidPathLength, label = "A*E", ls='dotted')
plt.xlabel('complexity')
plt.ylabel('path length')
plt.legend()

plt.subplot(3, 1, 2)
plt.plot(x_axis, dfsVisitedNum, label = "dfs")
plt.plot(x_axis, bfsVisitedNum, label = "bfs")
plt.plot(x_axis, astarManHatVisitedNum, label = "A*MH")
plt.plot(x_axis, astarEuclidVisitedNum, label = "A*E")
plt.legend()
plt.xlabel('complexity')
plt.ylabel('number of nodes visited')

plt.subplot(3, 1, 3)
plt.plot(x_axis, dfsRunTimeNum, label = "dfs")
plt.plot(x_axis, bfsRunTimeNum, label = "bfs")
plt.plot(x_axis, astarManHatRunTimeNum, label = "A*MH")
plt.plot(x_axis, astarEuclidRunTimeNum, label = "A*E")
plt.legend()
plt.xlabel('complexity')
plt.ylabel('run time')

plt.show()
