class Queue:
    def __init__(self, size):
        self.size = size
        self.container = [None] * size
        self.f = -1  # Front of the queue
        self.r = 0  # Next available cell

    def _enqueue(self, item):
        if self._isfull():
            print("Queue is Full")
            return
        if self.f == -1:
            self.f = 0
        self.container[self.r] = item
        self.r += 1
        
    def _dequeue(self):
        if self._isempty():
            print("Queue is Empty")
            return None
        item = self.container[self.f]
        self.container[self.f] = None
        self.f += 1
        return item

    def _isempty(self):
        return self.f == -1 or self.f==self.r

    def _isfull(self):
        return self.r == self.size

    def print_queue(self):
        if self._isempty():
            print("There is nothing to show!")
            return
        print("Front -> ", end="")
        i = self.f
        while i <= self.r-1:
            print(self.container[i], end=" ")
            i +=1
        print(" <- Rear")


# Example usage:
queue = Queue(5)

# Enqueuing elements into the queue
queue._enqueue(1)
queue._enqueue(2)
queue._enqueue(3)
queue._enqueue(4)
queue._enqueue(5)

queue.print_queue()

queue._enqueue(6)

queue.print_queue()
