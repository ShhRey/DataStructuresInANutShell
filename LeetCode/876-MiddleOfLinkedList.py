# Class to represent each Node of Linked List
class Node:
    def __init__(self, item):
        self.item = item
        self.next = None

# Class to represent Singly Linked List
class SinglyLL:
    def __init__(self) -> None:
        self.head = None

    # Function to Insert Elements after Head
    def insertAtEnd(self, item):
        new_node = Node(item)
        if not self.head:
            self.head = new_node
            return
        current_node = self.head
        while current_node.next:
            current_node = current_node.next
        current_node.next = new_node

    # Function to find Middle Node
    def middleNode(self):
        slowPointer = self.head
        fastPointer = self.head
        while (fastPointer is not None) and (fastPointer.next is not None):
            slowPointer = slowPointer.next
            fastPointer = fastPointer.next.next
        # Fetching all the Nodes after Middle to store in result
        result = []
        current_node = slowPointer
        while current_node:
            result.append(current_node.item)
            current_node = current_node.next
        return result

# Collecting Inputs from Users
arr = []
elementCount = int(input("Enter Total Elements you want to Add: "))
for i in range(1, elementCount+1):
    element = int(input(f"Adding Element {i} into Head: "))
    arr.append(element)

sll = SinglyLL()
for i in arr:
    sll.insertAtEnd(i)

print(sll.middleNode())