class Stack:

    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        return self.items.append(item)

    def pop(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    @property
    def printstack(self):
        for item in reversed(self.items):
            print(item)

s = Stack()
print(s.isEmpty())

s.push(6)
s.push(7)
s.push("Hello world!")
s.push("rtt")

s.pop()

print(s.size())

s.printstack

