class CircularQueue:
    def __init__(self, size):
        self.size = size
        self.queue = [None] * size
        self.head = self.tail = -1

    def enqueue(self, data):
        if (self.tail + 1) % self.size == self.head:
            return 'queue is full!'
        elif self.head == -1:
            self.head = 0
            self.tail = 0
        else:
            self.tail = (self.tail + 1) % self.size
        self.queue[self.tail] = data

    def dequeue(self):
        if self.head == -1:
            return 'queue is empty!'
        elif self.head == self.tail:
            temp = self.queue[self.tail]
            self.head = -1
            self.tail = -1
            return temp
        else:
            temp = self.queue[self.head]
            self.head = (self.head + 1) % self.size
            return temp

    def print(self):
        if self.tail >= self.head:
            for i in range(self.head, self.tail):
                print(self.queue[i], end="  ")
            print()
        else:
            for i in range(self.head, self.size):
                print(self.queue[i], end="  ")
            for i in range(0, self.tail):
                print(self.queue[i], end="  ")
            print()
    def isEmpty(self):
        return self.head == -1
    def isFull(self):
        return (self.tail + 1) % self.size == self.head
    def peek(self):
        return self.queue[self.head]
    def size(self):
        return self.size
    def clear(self):
        self.head = -1
        self.tail = -1
        self.queue = [None] * self.size
    def __str__(self):
        return str(self.queue)
    def delete(self):
        del self.queue

obj = CircularQueue(5)
obj.enqueue(1)
obj.enqueue(2)
obj.enqueue(3)
obj.enqueue(4)
obj.enqueue(5)
print("Initial queue")
obj.print()

obj.dequeue()
print("After removing an element from the queue")
obj.print()
