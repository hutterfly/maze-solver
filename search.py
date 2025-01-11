from collections import deque
import heapq as hq

def addEdgeFromMaze(graph, maze, cell):
    if maze[cell[0], cell[1]] == 1:
        return
    above = (cell[0] - 1, cell[1])
    below = (cell[0] + 1, cell[1])
    right = (cell[0], cell[1] + 1)
    left = (cell[0], cell[1] - 1)
    edges = []
    if above[0] > -1:
        if maze[above] == 0:
            edges.append(above)
    if below[0] < maze.shape[0]:
        if maze[below] == 0:
            edges.append(below)
    if right[1] < maze.shape[1]:
        if maze[right] == 0:
            edges.append(right)
    if left[1] > -1:
        if maze[left] == 0:
            edges.append(left)

    graph[cell] = edges

def addAllEdgesFromMaze(graph, maze):
    for i in range(maze.shape[0]):
        for j in range(maze.shape[1]):
            addEdgeFromMaze(graph, maze, (i, j))

def dfs(graph, node, endPoint, visited=None, nodesParents=None): #depth first search
    if visited == None:
        visited = []
    if nodesParents == None:
        nodesParents = {node : None}
    visited.append(node)
    if node == endPoint:
        return displaySolution(endPoint, nodesParents), visited
    for i in graph[node]:
        if i not in visited:
            nodesParents[i] = node
            foo = dfs(graph, i, endPoint, visited, nodesParents)
            if foo != None:
                return foo
    return None

def bfs(graph, startPoint, endPoint): #breadth first search
    nodeQueue = deque()
    nodeQueue.append(startPoint)
    visited = {startPoint}
    visitedarr = []
    nodesParents = {startPoint : None}
    while nodeQueue:
        e = nodeQueue.popleft()
        for i in graph[e]:
            if i not in visited:
                nodeQueue.append(i)
                visited.add(i)
                nodesParents[i] = e
                visitedarr.append(i)
            if i == endPoint:
                return displaySolution(endPoint, nodesParents), visitedarr

def displaySolution(node, nodesParents):
    path = [node]
    while nodesParents[node] != None:
        #print(node)
        path.append(nodesParents[node])
        node = nodesParents[node]
    path.reverse()
    return path

def aStar(graph, startPoint, endPoint, manOrEuclid):
    openListHeap = [(0, startPoint)] #(F, (y,x))
    openListDict = {startPoint : (0, 0)} #(y,x) : (G, H)
    closedListDict = {}
    nodesParents = {startPoint : None}
    visited = []
    while openListHeap:
        currentNode = hq.heappop(openListHeap)[1]
        currentNodeG, currentNodeH = openListDict[currentNode]
        if currentNode == endPoint:
            return displaySolution(endPoint, nodesParents), visited
        for i in graph[currentNode]:
            successorG = currentNodeG + 1
            successorH = aStarH(manOrEuclid, i, endPoint)
            successorF = successorG + successorH
            if i in openListDict:
                openG, openH = openListDict[i]
                if (openG + openH) <= successorF:
                    continue
            elif i in closedListDict:
                closedG, closedH = closedListDict[i]
                if (closedG + closedH) <= successorF:
                    continue
            hq.heappush(openListHeap, (successorF, i))
            openListDict[i] = (successorG, successorH)
            nodesParents[i] = currentNode
            visited.append(i)
        closedListDict[currentNode] = (currentNodeG, currentNodeH)

def aStarH(manOrEuclid, currentNode, endPoint):
    if manOrEuclid:
        return manhatDist(currentNode, endPoint)
    return euclideanDist(currentNode, endPoint)

def manhatDist(currentNode, endPoint):
    return abs(endPoint[0] - currentNode[0]) + abs(endPoint[1] - currentNode[1])

def euclideanDist(currentNode, endPoint):
    return (((endPoint[0] - currentNode[0]) ** 2) + ((endPoint[1] - currentNode[1]) ** 2)) ** 0.5
