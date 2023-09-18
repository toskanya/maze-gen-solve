from graph import *
import pygame
import math
import copy

class Maze():
    def __init__(self, maze_txt):
        self.start = ()
        self.end = ()
        self.grid = [[]]
        self.states = []
        self.row = 0
        self.col = 0
        
        for c in maze_txt:
            if c == "A":
                self.start = (self.row, self.col)
            if c == "B":
                self.end = (self.row, self.col)
            if c == "\n":
                self.grid.append([])
                self.row += 1
                self.col = 0
            else:
                self.grid[self.row].append(c)
                self.col += 1
        
        self.row += 1
    
    #print the initial maze
    def print(self):
        for row in self.grid:
            for col in row:
                if col == "#":
                    print("█", sep='  ', end='')
                elif col == " ":
                    print(" ", sep='  ', end='')
                else:
                    print(col, sep=' ', end='')
            print()

    # #print the solved maze
    # def printResult(self, result, explored=None):
    #     for y, row in enumerate(self.grid):
    #         for x, col in enumerate(row):
    #             if col == "#":
    #                 print("█", sep=' ', end='') 
    #             elif (y, x) in result:
    #                 print("*", sep=' ', end='')
    #             elif (y, x) in explored:
    #                 print("o", sep=' ', end='')
    #             elif col == " ":
    #                 print(" ", sep=' ', end='')
    #             else:
    #                 print(col, sep=' ', end='')
    #         print()

    #convert maze to graph
    def toGraph(self):        
        if not self.grid:
            return

        graph = Graph()

        for y, row in enumerate(self.grid):
            for x, col in enumerate(row):
                if self.grid[y][x] != "#":
                    if x > 0 and self.grid[y][x - 1] != "#":
                        graph.addEdge((y, x), (y, x - 1))
                    if y > 0 and self.grid[y - 1][x] != "#":
                        graph.addEdge((y, x), (y - 1, x))
                        
        return graph

    def addState(self, state):
        for y, row in enumerate(self.grid):
            for x, cell in enumerate(row):
                if (y, x) == state:
                    self.grid[y][x] = 'o'
        self.states.append(copy.deepcopy(self.grid))
        
    def draw(self):
        pygame.display.init()
        
        display_info = pygame.display.Info()
        scr_width, scr_height = display_info.current_w / 1.1, display_info.current_h / 1.1
        
        step_x, step_y = math.floor(scr_width / self.col), math.floor(scr_height / self.row)
        color = {
            "A": (225, 0, 0),
            "B": (0, 225, 0),
            "o": (150, 150, 225),
            "#": (0, 0, 0),
            " ": (225, 225, 225)
        }
        count = 0
        screen = pygame.display.set_mode((scr_width, scr_height))
        screen.fill((255, 255, 255))
        pygame.display.set_caption("Maze")

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                # if event.type == pygame.KEYDOWN:
                #     if event.key == pygame.K_BACKSPACE:
                #         running = False
            
            if count < len(self.states):
                for state in self.states:
                    x, y = 0, 0
                    for row in state:
                        for cell in row:
                            pygame.draw.rect(screen, color[cell], [x, y, step_x, step_y])
                            x += step_x
                        x = 0
                        y += step_y
                    pygame.time.delay(25)
                    pygame.display.flip()
                    count += 1
        pygame.display.quit()