from frontier import *

class QueueFrontier(Frontier):
    def add(self, node):
        self.frontier.append(node)
        
    def remove(self):
        if self.isEmpty():
            raise Exception("Frontier is empty")
        
        node = self.frontier[0]
        self.frontier = self.frontier[1:]
        return node