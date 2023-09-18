from graph import *
from maze import *
from stackfrontier import *
from pygame.locals import *
import pygame
import random
import copy

class Node:
    def __init__(self, state, parent=None):
        self.state = state
        self.parent = parent

def mazeGen(size):
    width, height = size
    
    #generating blank maze string
    blank = (" " * width + "\n") * height

    #generating template maze string
    template = ""
    template += "#" * width * 2 + "#" + "\n"
    for y in range(height):
        template += "#"
        for x in range(width):
            template += " #"
        template += "\n"
        template += "#" * width * 2 + "#" + "\n" 
    template = template[:-1]

    #convert blank to maze blank
    maze_blank = Maze(blank)
    
    #convert maze blank to graph
    graph = maze_blank.toGraph()
    
    #convert template maze into a matrix
    maze_template = Maze(template).grid
    
    #initializing frontier using stack and explored set 
    frontier = StackFrontier()
    explored = set()

    #randomizing start and end postion of the maze
    random_start = graph.getVertex(random.randint(0, width * height - 1))
    random_end = graph.getVertex(random.randint(0, width * height - 1))

    #add start node to the frontier
    start_node = Node(random_start)
    frontier.add(start_node)

    result = ""
    while True:
        #done generating maze
        if frontier.isEmpty():
            maze_template[random_start[0] * 2 + 1][random_start[1] * 2 + 1] = "A"
            maze_template[random_end[0] * 2 + 1][random_end[1] * 2 + 1] = "B"
            for row in maze_template:
                for cell in row:
                    result += cell
                result += "\n"
            break            
        
        #pop node out of the stack
        node = frontier.remove()
        
        #breaking the wall between current node and its parent
        pre = node.parent
        if pre:
            d_x = node.state[1] - pre.state[1]
            if d_x == 1:
                maze_template[node.state[0] * 2 + 1][node.state[1] * 2] = " "
            elif d_x == -1:
                maze_template[pre.state[0] * 2 + 1][pre.state[1] * 2] = " "
            d_y = node.state[0] - pre.state[0]
            if d_y == 1:
                maze_template[node.state[0] * 2][node.state[1] * 2 + 1] = " "
            elif d_y == -1:
                maze_template[pre.state[0] * 2][pre.state[1] * 2 + 1] = " "
        
        #add the popped node state to explored set
        explored.add(node.state)
        
        #update maze blank with maze template for drawing in pygame
        maze_blank.states.append(copy.deepcopy(maze_template))
        
        #create child to check if it exist
        child = None
        
        #use a loop to in case of no neighbour, we can backtrack
        #while we cant find a neighbour and we havent explore all
        while not child and len(explored) != width * height:
            #get neighbours of the node
            neighbours = graph.neighbour(node.state)
        
            #shuffle the neighbours
            random.shuffle(neighbours)
        
            #choose one neighbour
            for neighbour in neighbours:
                if not frontier.contain_state(neighbour) and neighbour not in explored:
                    child = Node(neighbour, node)
                    frontier.add(child)
                    break            
                
            #backtracking to where we can find a neighbour
            if not child:
                node = node.parent
    
    maze_blank.states.append(copy.deepcopy(maze_template))
    maze_blank.col = width * 2 + 1
    maze_blank.row = height * 2 + 1
    maze_blank.draw()
    return result[:-1]
    
        # for row in maze_template:
        #     for cell in row:
        #         print(cell, end='')
        #     print()
        # print()
