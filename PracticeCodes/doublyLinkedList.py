# Represent each Node of the Linked List
class Node:
    def __init__(self, item):
        self.item = item
        self.next = None
        self.prev = None

# Class to Represent Linked List
class DoublyLL:
    def __init__(self):
        self.head = None
        self.tail = None


    # Function to Add Item after Node
    def append(self, item):
        new_node = Node(item)
        if not self.head:
            self.head = new_node
            print(f"Creating {item} as the Head Node")
            return
        current_node = self.head
        while current_node.next:
            current_node = current_node.next
        current_node.next = new_node
        new_node.prev = current_node
        print(f"Appending {item} into the DoublyLL")

    
    # Function to Add Item after specific Node
    # def insertAfter(self, target, item):
    #     if target is None:
    #         print("Target Cannot be None")
    #     new_node = Node(item)
    #     new_node.next = target.next
    #     target.next = new_node
    #     new_node.prev = target
    #     while current_node:
    #         if current_node.item == target:
    #             new_node.next = current_node.next
    #             current_node.next = new_node
    #             return
    #         current_node = current_node.next
    #         print(f"Inserting {item} after Target {target}")
    #     print(f"Target Node {target} not Found ! Cannot insert {item}")


    # Function to Add Item before Head
    def prepend(self, item):
        new_node = Node(item)
        new_node.next = self.head
        self.head = new_node
        print(f"Prepending {item} before Head")

    # Function to Print DLL
    def displayDLL(self):
        current_node = self.head
        while current_node:
            print(current_node.item, end=" -> ")
            current_node = current_node.next
        print("None")


dll = DoublyLL()
dll.prepend(1)
dll.prepend(0)
dll.append(2)
dll.append(3)
dll.displayDLL()
