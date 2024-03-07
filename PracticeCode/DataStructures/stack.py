class Stack:
    def __init__(self):
        self.stack = []
        self.max_size = int(input("Enter Max Limit for Stack: "))


    # Function for Pushing Element into the Stack
    def push(self, item):
        if len(self.stack) < self.max_size:
            print(f"Inserting {item} into Stack")
            return self.stack.append(item)
        else:
            print(f"Stack is Full and cannot hold more than {self.max_size} items")


    # Function for Poping Element out of Stack
    def pop(self):
        if len(self.stack) > 0:
            print(f"Will Pop {self.stack[-1]} from Stack")
            return self.stack.pop()
        else:
            print("Stack Already Empty")


    # Function for Peeking into the Stack
    def peek(self):
        print(f"The Last Element in Stack: {self.stack[-1]}")
        return self.stack[-1]


    # Function to check if Stack is Empty or Not
    def is_empty(self):
        if len(self.stack) == 0:
            print("Stack is Empty")
            return not self.stack
        else:
            print("Stack Not Empty")
    

    # Function to check if Stack is Full or Not
    def is_full(self):
        if len(self.stack) >= self.max_size:
            print(f"Stack is Full after inserting {self.max_size} items !")
        else:
            space = self.max_size - len(self.stack)
            print(f"{space} Elements can be added before Stack is Full")

    # Function for returning the Size of the Stack
    def size(self):
        print(f"There are {len(self.stack)} Elements in Stack")
        return len(self.stack)


stack = Stack()
stack.pop()
stack.push('apple')
stack.push('banana')
stack.push('cherry')
stack.peek()
stack.size()
stack.pop()
stack.pop()
stack.pop()
stack.pop()