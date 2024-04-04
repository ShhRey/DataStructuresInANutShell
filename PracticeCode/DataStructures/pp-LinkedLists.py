# Question 1: Inserting Element at End
'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def display(self):
        current = self.head
        while current:
            print(current.data, end="->")
            current = current.next
        print("None")

if __name__ == "__main__":
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.append(4)
    ll.display()
'''

# Question 2: Delete Node at Given Position
'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def deletePos(self, position):
        if self.head is None:
            return
        if position == 0:
            self.head = self.head.next
            return
        current = self.head
        prev = None
        for _ in range(position):
            if current is None:
                return
            prev, current = current, current.next
        if prev and current:
            prev.next = current.next

    def display(self):
        current = self.head
        while current:
            print(current.data, end="->")
            current = current.next
        print("None")

ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.append(4)
ll.deletePos(2)
ll.display()
'''

# Question 3: Search for a Particular Element
'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def search(self, value):
        current = self.head
        while current:
            if current.data == value:
                return True
            current = current.next
        return False
    
ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.append(4)
element = 3
if ll.search(element):
    print(f"{element} found in LL")
else:
    print(f"{element} not in LL")
'''

# Question 4: Find length of Linked List
'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLL:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def length(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

ll = SinglyLL()
ll.append(1)
ll.append(2)
ll.append(3)
ll.append(4)
print(ll.length())
ll.display()
'''

# Question 5: Reverse the Nodes of Singly LL
'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLL:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    def display(self):
        current = self.head
        while current:
            print(current.data, end="->")
            current = current.next
        print("None")

ll = SinglyLL()
ll.append(1)
ll.append(2)
ll.append(3)
ll.append(4)
ll.reverse()
ll.display()
'''

# Question 6: Remove Duplicate Elements from Unsorted LL
'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
        
    def remDup(self):
        if self.head is None:
            return
        current = self.head
        prev = None
        seen = set()
        while current:
            if current.data in seen:
                prev.next =  current.next
            else:
                seen.add(current.data)
                prev = current
            current = current.next

    def display(self):
        current = self.head
        while current:
            print(current.data, end="->")
            current = current.next
        print("None")

ll = LinkedList()
ll.append(1)
ll.append(1)
ll.append(2)
ll.append(3)
ll.append(4)
ll.append(3)
ll.append(5)
ll.append(2)
ll.append(5)
ll.remDup()
ll.display()
'''

# Question 7: Move Last Node to First Node
'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def moveLF(self):
        if (self.head is None) or (self.head.next is None):
            return
        second_last = None
        last = self.head
        while last.next:
            second_last = last
            last = last.next
        second_last.next = None
        last.next = self.head
        self.head = last

    def display(self):
        current = self.head
        while current:
            print(current.data, end="->")
            current = current.next
        print("None")

ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.append(4)
ll.append(5)
ll.display()
ll.moveLF()
ll.display()
'''

# Question 8: Middle of Linked List
'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
        
    def findMid(self):
        if self.head is None:
            return
        slow_ptr = self.head
        fast_ptr = self.head

        while fast_ptr and fast_ptr.next:
            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next.next
        return slow_ptr
    
    def display(self):
        current = self.head
        while current:
            print(current.data, end="->")
            current = current.next
        print("None")
    
ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.append(4)
ll.append(5)
ll.display()
print(ll.findMid().data)
'''

# Question 9: Delete Nodes with greater value on Right
'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def reverse(self):
        current = self.head
        prev = None
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    def checkRight(self):
        if (self.head is None) or (self.head.next is None):
            return
        self.reverse()
        max_value = self.head.data
        current = self.head.next
        prev = self.head

        while current:
            if current.data < max_value:
                prev.next = current.next
                current = current.next
            else:
                max_value = current.data
                prev = current
                current = current.next
        self.reverse()

    def display(self):
        current = self.head
        while current:
            print(current.data, end="->")
            current = current.next
        print("None")

ll = LinkedList()
ll.append(12)
ll.append(15)
ll.append(10)
ll.append(11)
ll.append(5)
ll.append(6)
ll.append(2)
ll.append(3)
ll.display()
ll.checkRight()
ll.display()
'''

# Question 10: Cycle Detection in LL
'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def Cycle(self):
        if self.head is None:
            return
        slow_ptr = self.head
        fast_ptr = self.head

        while fast_ptr and fast_ptr.next:
            if slow_ptr == fast_ptr:
                return True
            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next.next
        return False

    def display(self):
        current = self.head
        while current:
            print(current.data, end="->")
            current = current.next
        print("None")

ll = LinkedList()
ll.append("A")
ll.append("B")
ll.append("C")
ll.append("D")
ll.append("E")
ll.append("C")
if ll.Cycle():
    print("Cycle")
else:
    print("No Cycle")
'''