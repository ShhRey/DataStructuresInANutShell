class Node:
    def __init__(self, element=None):
        self.element = element
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insertAfter(self, p, e):
        if p is None:
            #First node:
            new_node = Node(e)
            new_node.next=None
            new_node.pre=None
            self.head=new_node
            self.tail=new_node
            return

        new_node = Node(e)

        # Adjust pointers
        new_node.next = p.next
        if p.next:#if we p is not tail
            p.next.prev = new_node
        p.next = new_node
        new_node.prev = p

        # Update tail if necessary
        if p == self.tail:
            self.tail = new_node

    def remove(self, p):
        if p is None:
            print("Cannot remove a None node.")
            return

        # Adjust pointers
        t=p.element
        if p.prev:#if p is not head
            p.prev.next = p.next
        else:#if p is head
            self.head = p.next

        if p.next:#if p is not tail
            p.next.prev = p.prev
        else: #if p is tail
            self.tail = p.prev

        # Clear pointers from the removed node
        p.prev = None
        p.next = None
        return t

    def display(self):
        current = self.head
        while current:
            print(current.element, end=" ")
            current = current.next
        print()


# Example usage:

dll = DoublyLinkedList()
dll.insertAfter(None, 5)  # single node
dll.display()  # Output: 5 

dll.insertAfter(dll.head, 3)  # Insert 3 after 5
dll.insertAfter(dll.head.next, 7)  # Insert 7 after 3

print("Doubly Linked List:")
dll.display()  # Output: 5 3 7

dll.remove(dll.head)  # Remove the first node
print("After removing the first node:")
dll.display()  # Output: 3 7

dll.remove(dll.tail)  # Remove the last node
print("After removing the last node:")
dll.display()  # Output: 3
