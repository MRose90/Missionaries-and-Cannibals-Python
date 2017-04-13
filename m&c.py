# -*- coding: utf-8 -*-
#Python 2.7
"""
@author: Michael Rose, Jacob Broderick
"""
import sys
import Queue

visited = []
#STATES = [Missionary Left, Cannibal Left, Boat Left, Missionary Right, Cannibal Right, Boat Right]
#Put one missionary in the boat
def succ1(ini):
    #boat on left
    if ini[2] == 1:
        return [ini[0]-1,ini[1],0,ini[3]+1,ini[4],1]
    return [ini[0]+1,ini[1],1,ini[3]-1,ini[4],0]
    
#Put two missionaries in the boat
def succ2(ini):
    #boat on left
    if ini[2] == 1:
        return [ini[0]-2,ini[1],0,ini[3]+2,ini[4],1]
    return [ini[0]+2,ini[1],1,ini[3]-2,ini[4],0]
        
#Put one cannibal in the boat
def succ3(ini):
    #boat on left
    if ini[2] == 1:
        return [ini[0],ini[1]-1,0,ini[3],ini[4]+1,1]
    return [ini[0],ini[1]+1,1,ini[3],ini[4]-1,0]

#Put one cannibal and one missionary in the boat      
def succ4(ini):
    #boat on left
    if ini[2] == 1:
        return [ini[0]-1,ini[1]-1,0,ini[3]+1,ini[4]+1,1]
    return [ini[0]+1,ini[1]+1,1,ini[3]-1,ini[4]-1,0]

#Put two cannibals in the boat   
def succ5(ini):
    #boat on left
    if ini[2] == 1:
        return [ini[0],ini[1]-2,0,ini[3],ini[4]+2,1]
    return [ini[0],ini[1]+2,1,ini[3],ini[4]-2,0]

#Checks the validity of the state for missionaries and cannibals.
def isValid(state):
    if state[0]<state[1] and state[0] > 0 or state[3]<state[4] and state[3]> 0 or state[0] < 0 or state [1] < 0 or state[3] < 0 or state [4] < 0:
        return False
    return True

#Breadth first search
def bfs(ini,goal):
    #initialize
    counter= 0
    q = [[ini,""]]
    #the loop
    while q:
        #stores and removes first value of queue
        cur = q.pop(0)
        #WE WANT THIS TO HAPPEN!
        if cur[0] == goal:
            return [cur[1],counter]
        #Checks validity of state and if the state has already been seen
        if isValid(cur[0]) == True and not(cur[0] in visited):   
            #Adds state to visited states
            visited.append(cur[0])
            #Adds future states to queue
            q.append([succ1(cur[0]),cur[1]+"1"])
            q.append([succ2(cur[0]),cur[1]+"2"])
            q.append([succ3(cur[0]),cur[1]+"3"])
            q.append([succ4(cur[0]),cur[1]+"4"])
            q.append([succ5(cur[0]),cur[1]+"5"])
        counter += 1
    #Not possible to solve (This should not happen)
    return [None,counter]

#Parses our string of moves into actual states
def output_parse(arr,ini,out):
    state = ini
    of = open(out,'w')
    of.write(str(state))
    #Prints initial state
    print(state)
    #n values based on helper functions and order given.
    for n in arr[0]:
        if n == '1':
            state = succ1(state)
        elif n == '2':
            state = succ2(state)
        elif n == '3':
            state = succ3(state)
        elif n == '4':
            state = succ4(state)
        elif n == '5':
            state = succ5(state)
        else:
            #Uh oh
            of.write("The boat sank.")
            print("The boat sank.")
            of.close()
            return
        of.write("\n"+str(state))
        print(state)
    print("\nIt took "+str(len(arr[0]))+" moves.")
    print("\nIt opened "+str(arr[1])+" nodes.")
    of.close()
   
#Depth first search
def dfs(ini,goal):
    if ini == goal:
        return ["",0]
    if not isValid(ini):
        return [None,1]
    #Avoids infinite loops
    if ini in visited:
        return [None,1]
    visited.append(ini)
    counter = 1
    #The recursive part
    retValue = dfs(succ1(ini),goal)
    counter += retValue[1]
    if retValue[0] is not None:
        return ["1"+retValue[0],counter]
    retValue = dfs(succ2(ini),goal)
    counter += retValue[1]
    if retValue[0] is not None:
        return ["2"+retValue[0],counter]
    retValue = dfs(succ3(ini),goal)
    counter += retValue[1]
    if retValue[0] is not None:
        return ["3"+retValue[0],counter]
    retValue = dfs(succ4(ini),goal)
    counter += retValue[1]
    if retValue[0] is not None:
        return ["4"+retValue[0],counter]
    retValue = dfs(succ5(ini),goal)
    counter += retValue[1]
    if retValue[0] is not None:
        return ["5"+retValue[0],counter]
    return [None,counter]

def iddfs(ini,goal,depth):
    if depth == 0 and ini == goal:
        return ["",0]
    if not isValid(ini):
        return [None,1]
    #This is what can make it different from BFS
    if ini in visited:
        return [None,1]
    visited.append(ini)
    counter = 1
    #Only iterate until desired depth
    if depth > 0:
        retValue = iddfs(succ1(ini),goal,depth-1)
        counter += retValue[1]
        if retValue[0] is not None:
            return ["1"+retValue[0],counter]
        retValue = iddfs(succ2(ini),goal,depth-1)
        counter += retValue[1]
        if retValue[0] is not None:
            return ["2"+retValue[0],counter]
        retValue = iddfs(succ3(ini),goal,depth-1)
        counter += retValue[1]
        if retValue[0] is not None:
            return ["3"+retValue[0],counter]
        retValue = iddfs(succ4(ini),goal,depth-1)
        counter += retValue[1]
        if retValue[0] is not None:
            return ["4"+retValue[0],counter]
        retValue = iddfs(succ5(ini),goal,depth-1)
        counter += retValue[1]
        if retValue[0] is not None:
            return ["5"+retValue[0],counter]
    return [None,counter]    

#Finds neighbors for astar
def neighbors(state):
    n = []
    temp = succ1(state)
    if isValid(temp):
        n.append([temp,"1"])
    temp = succ2(state)
    if isValid(temp):
        n.append([temp,"2"])
    temp = succ3(state)
    if isValid(temp):
        n.append([temp,"3"])
    temp = succ4(state)
    if isValid(temp):
        n.append([temp,"4"])
    temp = succ5(state)
    if isValid(temp):
        n.append([temp,"5"])
    return n

#heuristic for astar
def heuristic(parent,child):
    return abs(parent[0]+parent[1]-(child[0]+child[1]))+abs(parent[3]+parent[4]-(child[3]+child[4]))

#Uses weighted nodes to find best path
def astar(ini,goal):
    s = ''
    pqueue = Queue.PriorityQueue()
    #PQueue uses format ([State,previous steps], priority)
    pqueue.put([ini,""], 0)
    cost = {}
    key = s.join(str(v) for v in ini)
    cost[key] = 0
    counter = 0
    #Loops over all possibilities until a solution is found or there are none
    while not pqueue.empty():
        current = pqueue.get()
        if current[0] == goal:
            return [current[1],counter]
        counter += 1
        n = neighbors(current[0])
        for node in n:
            key = s.join(str(v) for v in current[0])
            node_key = s.join(str(v) for v in node[0])
            new_cost = cost[key] + heuristic(current[0],node[0])
            #Only add the node if it is cheaper or doesn't exist yet
            if node_key not in cost or new_cost < cost[node_key]:
                cost[node_key] = new_cost
                pqueue.put([node[0],current[1]+node[1]],new_cost)
    return [None,counter]

#setup for printing and displaying, calls actual algorithms
def bfsSetup(ini, goal, out):
    s = bfs(ini,goal)
    output_parse(s,ini,out)
    return s

def dfsSetup(ini, goal, out):
    s = dfs(ini,goal)
    output_parse(s,ini,out)
    return s

#Because of the nature this one also partially implements the algorithm (updates the max depth)
def iddfsSetup(ini, goal, out):
    depth = 0
    maxNodes = 0
    while True: 
        s = iddfs(ini,goal,depth)
        if s[0] is not None:
            break
        if s[1] > maxNodes:
            maxNodes = s[1]
        depth += 1
        #if we don't clear it won't end because the first node has been visited
        visited[:] = []
    output_parse(s,ini,out)
    print("Largest number of nodes opened on a failed run was: " + str(maxNodes))
    return s

def astarSetup(ini, goal, out):
    s = astar(ini,goal)
    output_parse(s, ini, out)
    return s

#Converts the input files to a state
def getState(fileName):
    fo = open(fileName,"r")
    state = list(map(int,fo.readline().rstrip().split(",") +fo.readline().rstrip().split(",")))
    fo.close()
    return state
    
#This code is pretty ugly but basically runs over every instance
def allOutput():
    out = []
    iniState = getState("start1.txt")
    goalState = getState("goal1.txt")
    output = "output.txt"
    out.append("Order = bfs, dfs, iddfs, astar")
    out.append("Order = Length of path, Number of nodes")    
    out.append("\nTest 1")
    b = bfsSetup(iniState,goalState,output)
    out.append([str(len(b[0])),b[1]])
    visited[:] = []
    d = dfsSetup(iniState,goalState,output)
    out.append([str(len(d[0])),d[1]])
    visited[:] = []
    i = iddfsSetup(iniState,goalState,output)
    out.append([str(len(i[0])),i[1]])
    visited[:] = []
    a = astarSetup(iniState,goalState,output)
    out.append([str(len(a[0])),a[1]])
    visited[:] = []
    iniState = getState("start2.txt")
    goalState = getState("goal2.txt")
    out.append("\nTest 2")
    b = bfsSetup(iniState,goalState,output)
    out.append([str(len(b[0])),b[1]])
    visited[:] = []
    d = dfsSetup(iniState,goalState,output)
    out.append([str(len(d[0])),d[1]])
    visited[:] = []
    i = iddfsSetup(iniState,goalState,output)
    out.append([str(len(i[0])),i[1]])
    visited[:] = []
    a = astarSetup(iniState,goalState,output)
    out.append([str(len(a[0])),a[1]])
    visited[:] = []
    iniState = getState("start3.txt")
    goalState = getState("goal3.txt")
    out.append("\nTest 3")
    b = bfsSetup(iniState,goalState,output)
    out.append([str(len(b[0])),b[1]])
    visited[:] = []
    d = dfsSetup(iniState,goalState,output)
    out.append([str(len(d[0])),d[1]])
    visited[:] = []
    i = iddfsSetup(iniState,goalState,output)
    out.append([str(len(i[0])),i[1]])
    visited[:] = []
    a = astarSetup(iniState,goalState,output)
    out.append([str(len(a[0])),a[1]])
    of = open("tableData.txt",'w')
    for a in out:
        of.write(str(a)+"\n")
    of.close()
        
def main(argv):
    if argv[0] == "a":
        allOutput()
        return
    iniState = getState(argv[0])
    goalState = getState(argv[1])
    #Validation to confirm there is a possibly solution
    if (sum(iniState) != sum(goalState) or 
    iniState[0]+iniState[3] != goalState[0]+goalState[3] or  
    iniState[1]+iniState[4] != goalState[1]+goalState[4] or
    not(iniState[2]+iniState[5] == 1) or
    not(isValid(iniState)) or not(isValid(goalState))):
        print("Initial state cannot reach goal state.")
        return
    outputFile = argv[3]
    if argv[2] == "bfs":
        bfsSetup(iniState, goalState, outputFile)
    if argv[2] == "dfs":
        print("here")
        dfsSetup(iniState, goalState, outputFile)
    if argv[2] == "iddfs":
        iddfsSetup(iniState, goalState, outputFile)
    if argv[2] == "astar":
        astarSetup(iniState, goalState, outputFile)

if __name__ == '__main__':
    main(sys.argv[1:])