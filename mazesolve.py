from graph import *
from maze import *
from priorityqueuefrontier import *
from queuefrontier import *
from stackfrontier import *

#node representing cell of the maze containing properties:
#state: represent the coord of the node
#parent: link to the previous node (reversed linked list)
#step: amount of step made until this node
#cost: the manhattan distance between the node and the end node
class Node():
    def __init__(self, state, parent=None, cost=0):
        self.state = state
        self.parent = parent
        self.step = 0
        self.cost = cost
        
class SolveMaze():
    def __init__(self):
        self.result = list()
    
    #match case
    def solve(self, maze, type):     
        match type:
            case 'BFS':
                self.BFSnDFS(maze, QueueFrontier())
            case 'DFS':
                self.BFSnDFS(maze, StackFrontier())
            case 'GBFS':
                self.greedyBestFirstSearch(maze)
            case 'A*':
                self.AStar(maze)
    
    def greedyBestFirstSearch(self, maze):
        #convert maze to graph
        graph = maze.toGraph()
        explored = set()
        
        #initializing priorityQueue
        frontier = PriorityQueueFrontier()
        
        #initializing start node 
        start_node = Node(maze.start, cost=abs(maze.end[0] - maze.start[0]) + abs(maze.end[1] - maze.start[1]))
        
        #add start node to the frontier
        frontier.add(start_node)
        
        while True:
            if frontier.isEmpty():
                raise Exception("No Solution")
            
            #remove node from stack
            node = frontier.remove()
            
            #add node to visited list
            if node.state != maze.start and node.state != maze.end:
                explored.add(node.state)
                maze.addState(node.state)
            
            #if reach the goal
            if node.state == maze.end:
                actions = []
                
                #backtracking to the start
                node = node.parent
                while node.parent is not None:
                    actions.append(node.state)
                    node = node.parent
                
                #reverse the actions
                actions.reverse()
                self.result.append(actions)
                self.result.append(len(explored))
                self.result.append(explored)
                return
            
            #get the adjacent nodes of the current node
            neighbours = graph.neighbour(node.state)
            for neighbour in neighbours:
                
                #check if the neighbour is already in the frontier and explored
                if not frontier.contain_state(neighbour) and neighbour not in explored:
                    
                    #add property: parent = node, cost = manhattan distance
                    child = Node(neighbour, node, abs(maze.end[0] - neighbour[0]) + abs(maze.end[1] - neighbour[1]))
                    frontier.add(child)
    
    def BFSnDFS(self, maze, frontier):
        graph = maze.toGraph()
        explored = set()
         
        start_node = Node(maze.start)
        frontier.add(start_node)
        
        while True:
            if frontier.isEmpty():
                raise Exception("No Solution")
            
            #remove node from stack
            node = frontier.remove()
            
            #add node to visited list
            if node.state != maze.start and node.state != maze.end:
                explored.add(node.state)
                maze.addState(node.state)
            
            #if reach the goal
            if node.state == maze.end:
                actions = []
                
                #backtracking to the start
                node = node.parent
                while node.parent is not None:
                    actions.append(node.state)
                    node = node.parent
                
                #reverse the actions
                actions.reverse()
                self.result.append(actions)
                self.result.append(len(explored))
                self.result.append(explored)
                return
            
            #get the adjacent nodes of the current node
            neighbours = graph.neighbour(node.state)
            for neighbour in neighbours:
                
                #check if the neighbour is already in the frontier and explored
                if not frontier.contain_state(neighbour) and neighbour not in explored:
                    child = Node(neighbour, node)
                    frontier.add(child)

    def AStar(self, maze):
        graph = maze.toGraph()
        explored = set()
        frontier = PriorityQueueFrontier()
        start_node = Node(maze.start)
        frontier.add(start_node)
        self.result = []
        
        while True:
            #check if frontier is empty
            if frontier.isEmpty():
                raise Exception("No Solution")
            
            #remove node from the frontier
            node = frontier.remove()
            
            #add node to explored set
            if node.state != maze.start and node.state != maze.end:
                explored.add(node.state)
                maze.addState(node.state)
            
            #check if state is the solution
            if node.state == maze.end:
                actions = []
                
                node = node.parent
                while node.parent != None:
                    actions.append(node.state)
                    node = node.parent
                
                actions.reverse()
                self.result.append(actions)
                self.result.append(len(explored))
                self.result.append(explored)
                return
                
            #get the adjacent nodes of the current node
            neighbours = graph.neighbour(node.state)
            for neighbour in neighbours:

                #check if the neighbour is already in the frontier and explored
                if not frontier.contain_state(neighbour) and neighbour not in explored:
                    
                    #add property: parent = node, cost = manhattan distance
                    child = Node(neighbour, node, abs(maze.end[0] - neighbour[0]) + abs(maze.end[1] - neighbour[1]))
                    
                    #update the cost with the traveled steps
                    child.step = node.step + 1
                    child.cost += child.step
                    frontier.add(child)
  