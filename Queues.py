class Queue:

    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def inQ(self,item):
        self.items.insert(0,item)

    def deQ(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    def printQ(self):
        for i in self.items:
            print(i, end=' ')

q = Queue()
q.isEmpty()
q.inQ(34)
q.inQ("545")
q.inQ("Hello Friend")
q.printQ()
print()
q.deQ()
q.printQ()
q.isEmpty()
