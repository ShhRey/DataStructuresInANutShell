class Queue:
    def __init__(self):
        self.queue = []
        self.max_size = int(input("Enter Max Limit for Queue: "))
       
    # Function for Pushing Element into the Queue
    def enqueue(self, item):
        if len(self.queue) < self.max_size:
            print(f"Inserting {item} into Queue")
            return self.queue.append(item)
        else:
            print(f"Queue is Full and cannot hold more than {self.max_size} items")
    

    # Function for Poping Element out of Queue
    def dequeue(self):
        if len(self.queue) > 0:
            print(f"Will Pop {self.queue[0]} from Queue")
            return self.queue.pop(0)
        else:
            print("Queue Already Empty") 
    

    # Function for checking if Queue is Empty or Not
    def is_empty(self):
        if len(self.queue) == 0:
            print("Queue is Empty")
            return not self.queue
        else:
            print("Queue Not Empty") 
        
    
    # Function for checking if Queue is Full or Not
    def is_full(self):
        if len(self.queue) >= self.max_size:
            print(f"Queue is Full after inserting {self.max_size} items !")
        else:
            space = self.max_size - len(self.queue)
            print(f"{space} Elements can be added before Queue is Full")

        
    # Function for returning the Size of the Queue
    def size(self):
        print(f"There are {len(self.queue)} Elements in Queue")
        return len(self.queue)
        

queue = Queue()
queue.is_empty()
queue.enqueue('1')
queue.enqueue('2')
queue.enqueue('3')
queue.enqueue('4')
queue.is_full()
queue.enqueue('5')
queue.enqueue('6')
queue.is_empty()
queue.dequeue()
queue.dequeue()
queue.dequeue()
queue.dequeue()
queue.dequeue()
queue.dequeue()
queue.dequeue()
queue.dequeue()