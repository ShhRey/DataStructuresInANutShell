# Represent each Node of the Linked List
class Node:
    def __init__(self, item):
        self.item = item
        self.next = None


# Class to Represent Linked List
class SinglyLL:
    def __init__(self):
        self.head = None

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
        print(f"Appending {item} into the SinglyLL")

    # Function to Add Item after specific Node
    def insertAfter(self, target, item):
        new_node = Node(item)
        current_node = self.head
        while current_node:
            if current_node.item == target:
                print(f"Inserting {item} after Target {target}")
                new_node.next = current_node.next
                current_node.next = new_node
                return
            current_node = current_node.next
        print(f"Target Node {target} not Found ! Cannot insert {item}")
        

    # Function to Add Item before Head
    def prepend(self, item):
        new_node = Node(item)
        new_node.next = self.head
        self.head = new_node
        print(f"Prepending {item} before Head")

    # Function to Add Item before specific Node
    # def insertBefore(self, target, item):    
    #     new_node = Node(item)
    #     if not self.head:
    #         print(f"LinkedList is Empty. Cannot Insert {item} before {target}")
    #         return
    #     current_node = self.head
    #     while current_node:
    #         if current_node.item == target:
    #             current_node.next = new_node
    #         current_node = self.head
    #         print(f"Inserting {item} before Target {target}")
    #     print(f"Target Node {target} not Found ! Cannot insert {item}")
        

    # Function to Search a Node
    def search(self, item):
        target = item
        current_node = self.head
        while current_node:
            if current_node.item == target:
                print(f"{item} Present in LinkedList")
                return
            current_node = current_node.next
        print(f"{item} Not Found")


    # Function to Display LL with Nodes
    def displaySLL(self):
        current_node = self.head
        while current_node:
            print(current_node.item, end=" -> ")
            current_node = current_node.next
        print("None")

sll = SinglyLL()
sll.append(2)
sll.append(3)
sll.append(4)
sll.append(6)
sll.prepend(1)
sll.prepend(0)
sll.insertAfter(4, 5)
sll.search(4)
sll.displaySLL()

