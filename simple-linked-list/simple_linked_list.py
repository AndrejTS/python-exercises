class Node:
    def __init__(self, data):
        self.data = data
        self.next_element = None

    def value(self):
        return self.data

    def next(self):
        return self.next_element


class LinkedList:
    def __init__(self, values=[]):
        self._head = None
        self._len = 0
        for i in values:
            self.push(i)

    def __iter__(self):
        return self

    def __next__(self):
        if self._head == None:
            raise StopIteration
        output = self._head.data
        self._head = self._head.next_element
        return output

    def __len__(self):
        return self._len

    def head(self):
        if self._head:
            return self._head
        else:
            raise EmptyListException('List is empty')

    def push(self, value):
        if self._len == 0:
            self._head = Node(value)
        else:
            new_head = Node(value)
            new_head.next_element = self._head
            self._head = new_head
        self._len += 1 

    def pop(self):
        if self._len != 0:
            output = self._head.value()
            self._head = self._head.next()
            self._len -= 1
            return output
        else:
            raise EmptyListException('List is empty')

    def reversed(self):
        return LinkedList(self)


class EmptyListException(Exception):
    pass

