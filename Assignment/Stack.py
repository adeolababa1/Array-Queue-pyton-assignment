
# Stack Implementation Using Python

class Stack:
    def __init__(self, capacity):
        self.stack = []
        self.capacity = capacity

    # Push operation
    def push(self, item):
        if self.is_full():
            print("Stack Overflow! Stack is Full.")
        else:
            self.stack.append(item)
            print(item, "pushed into the stack.")

    # Pop operation
    def pop(self):
        if self.is_empty():
            print("Stack Underflow! Stack is Empty.")
        else:
            removed = self.stack.pop()
            print(removed, "popped from the stack.")

    # Check if stack is empty
    def is_empty(self):
        return len(self.stack) == 0

    # Check if stack is full
    def is_full(self):
        return len(self.stack) == self.capacity

    # Size operation
    def size(self):
        print("Stack size:", len(self.stack))

    # Peek operation
    def peek(self):
        if self.is_empty():
            print("Stack is Empty!")
        else:
            print("Top element:", self.stack[-1])

    # Display stack
    def display(self):
        print("Stack:", self.stack)


# Main program
s = Stack(5)

s.push(10)
s.push(20)
s.push(30)

s.display()
s.peek()

s.pop()
s.display()

print("Is Stack Empty?", s.is_empty())
print("Is Stack Full?", s.is_full())

s.size()
