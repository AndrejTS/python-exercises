class Node:
    def __init__(self, value, succeeding=None, previous=None):
        self.value = value
        self.succeeding = succeeding
        self.previous = previous


class LinkedList:
    def __init__(self):
        self.len = 0
        self.actual = None


    def __iter__(self):
        current = self.actual
        while current.previous != None:
            current = current.previous
        self.n = current
        return self


    def __next__(self):
        if self.n == None:
            raise StopIteration
        output = self.n.value
        self.n = self.n.succeeding
        return output


    def __len__(self):
        return self.len
        

    def push(self, value):
        if self.actual == None:
            self.actual = Node(value)
        else:
            self.actual.succeeding = Node(value, previous=self.actual)
            self.actual = self.actual.succeeding
        self.len += 1 


    def pop(self):
        output = self.actual.value
        self.actual = self.actual.previous
        if self.actual:
            self.actual.succeeding = None
        self.len -= 1
        return output


    def shift(self):
        current = self.actual
        while current.previous != None:
            current = current.previous
        output = current.value
        first = current.succeeding
        if first:
            first.previous = None
        self.len -= 1
        return output


    def unshift(self, value):
        if self.actual == None:
            self.actual = Node(value)
        else:
            current = self.actual
            while current.previous != None:
                current = current.previous
            current.previous = Node(value, succeeding=current)
            self.len += 1

