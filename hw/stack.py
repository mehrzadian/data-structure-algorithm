import sys
class stack:

    def __init__(self,capacity):
        self.items = []
        self.capacity=  capacity

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        if len(self.items) == self.capacity:
            raise Exception("Stack is full")
        self.items.append(item)

    def pop(self):
        if len(self.items) == 0:
            raise Exception("Stack is empty")
        return self.items.pop()

    def peek(self):
        if len(self.items) == 0:
            return sys.maxsize
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)
    def __str__(self):
        return str(self.items)