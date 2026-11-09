
# Queue Implementation Using Python

class Queue:
    def __init__(self, capacity):
        self.queue = []
        self.capacity = capacity

    # Enqueue operation
    def enqueue(self, item):
        if self.is_full():
            print("Queue is Full!")
        else:
            self.queue.append(item)
            print(item, "inserted into the queue.")

    # Dequeue operation
    def dequeue(self):
        if self.is_empty():
            print("Queue is Empty!")
        else:
            removed = self.queue.pop(0)
            print(removed, "removed from the queue.")

    # Check if queue is empty
    def is_empty(self):
        return len(self.queue) == 0

    # Check if queue is full
    def is_full(self):
        return len(self.queue) == self.capacity

    # Peek operation
    def peek(self):
        if self.is_empty():
            print("Queue is Empty!")
        else:
            print("Front element:", self.queue[0])

    # Display queue
    def display(self):
        print("Queue:", self.queue)


# Main program
q = Queue(5)

q.enqueue(10)
q.enqueue(20)
q.enqueue(30)

q.display()
q.peek()

q.dequeue()
q.display()

print("Is Queue Empty?", q.is_empty())
print("Is Queue Full?", q.is_full())
