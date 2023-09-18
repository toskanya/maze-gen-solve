from frontier import *
import math

class PriorityQueueFrontier(Frontier):
    def _leftChildIndex(self, index):
        return index * 2 + 1
    
    def _rightChildIndex(self, index):
        return index * 2 + 2
    
    def _parent(self, index):
        return math.floor((index - 1) / 2)
    
    def _hasLeftChild(self, index):
        return self._leftChildIndex(index) < len(self.frontier)
    
    def _hasRightChild(self, index):
        return self._rightChildIndex(index) < len(self.frontier)
    
    def _hasParent(self, index):
        return self._parent(index) >= 0
    
    #move the smallest node up the tree
    def _heapifyUp(self):
        index = len(self.frontier) - 1
        while (self._hasParent(index) and self.frontier[index].cost < self.frontier[self._parent(index)].cost):
            self.frontier[index], self.frontier[self._parent(index)] = self.frontier[self._parent(index)], self.frontier[index]
            index = self._parent(index)
    
    #move the biggest node down the tree
    def _heapifyDown(self):
        index = 0
        while (self._hasLeftChild(index)):
            smallerIndex = self._leftChildIndex(index)
            if (self._hasRightChild(index) and self.frontier[self._rightChildIndex(index)].cost < self.frontier[self._leftChildIndex(index)].cost):
                smallerIndex = self._rightChildIndex(index)
            
            if (self.frontier[smallerIndex].cost > self.frontier[index].cost):
                break
            else:
                self.frontier[smallerIndex], self.frontier[index] = self.frontier[index], self.frontier[smallerIndex]
            
            index = smallerIndex
            
    def add(self, node):
        self.frontier.append(node)
        self._heapifyUp()
        
    def remove(self):
        if self.isEmpty():
            raise Exception("Frontier is empty")
        
        node = self.frontier[0]
        self.frontier[0] = self.frontier[-1]
        self.frontier = self.frontier[:-1]
        self._heapifyDown()
        return node