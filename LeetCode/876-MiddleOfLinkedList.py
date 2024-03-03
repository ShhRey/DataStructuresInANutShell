# Class to represent each Node of Linked List
class Node:
    def __init__(self, item):
        self.item = item
        self.next = None
        self.prev = None


# Class to Represent Linked List
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None