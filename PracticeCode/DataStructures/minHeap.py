# Defining Class for Heap Data Structure
class MinHeap:
    def __init__(self):
        self.heap = []

    # Functions for Changing Parent and Child Node positions acc to heap
    def up_heap(self, index):
        parent_index = (index-1) // 2
        if (index > 0) and (self.heap[index] < self.heap[parent_index]):
            self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
            self.up_heap(parent_index) 
    
    def down_heap(self, index):
        pass

    # Function for adding New Elements at end of Heap
    def insert(self, item):
        self.heap.append(item)
        self.up_heap(len(self.heap) - 1)

    # Function for removing Last Element from Heap
    def remove(self):
        if len(self.heap) > 1:
            self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
            min_val = self.heap.pop()
            self.down_heap(0)
        elif self.heap:
            min_val = self.heap.pop()
        else:
            print("Heap Empty, No Elements to Pop")
            return None
        return min_val