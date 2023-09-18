class Frontier():
    def __init__(self):
        self.frontier = []
        
    def add(self, node):
        self.frontier.append(node)
    
    def remove(self):
        if self.isEmpty():
            raise Exception("Frontier is empty")
        
        node = self.frontier[-1]
        self.frontier = self.frontier[:-1]
        return node
    
    def isEmpty(self):
        return len(self.frontier) == 0

    def contain_state(self, state):
        for node in self.frontier:
            if (node.state == state):
                return True
        return False
    
    def print(self):
        print(self.frontier)