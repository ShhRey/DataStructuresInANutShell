class PriorityQueue:
    def __init__(self):
        self.queue = []

    # Function to Insert elements into PQ
    def insert(self, key, item):
        print(f"Inserting {item} into PQ with key {key}")
        self.queue.append((key, item))
        # Here we use reverse to bring the Element with highest priority first
        self.queue.sort(reverse=True)

    # Function to Remove elements from PQ
    def remove(self):
        if not self.queue:
            print("Queue is Empty")
        else:
            print(f"Removing the Element with Highest Priority: {self.queue[0]}")
            return self.queue.pop(0)
        

pq = PriorityQueue()
pq.insert(1, 'a')
pq.insert(3, 'c')
pq.insert(2, 'b')

print(pq.remove())
print(pq.remove())
print(pq.remove())
print(pq.remove())