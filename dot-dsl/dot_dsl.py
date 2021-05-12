NODE, EDGE, ATTR = range(3)


class Node:
    def __init__(self, name, attrs):
        self.name = name
        self.attrs = attrs

    def __eq__(self, other):
        return self.name == other.name and self.attrs == other.attrs


class Edge:
    def __init__(self, src, dst, attrs):
        self.src = src
        self.dst = dst
        self.attrs = attrs

    def __eq__(self, other):
        return (self.src == other.src and
                self.dst == other.dst and
                self.attrs == other.attrs)


class Graph:
    def __init__(self, data=None):
        self.nodes = []
        self.edges = []
        self.attrs = {}
        if data == None:
            return
        for i in data:
            if type(i) != tuple:
                raise TypeError('malformed graph')
            if len(i) != 3 and len(i) != 4:
                raise TypeError('malformed graph item')
            if i[0] == 0:
                if len(i) != 3:
                    raise ValueError('malformed node')
                self.nodes.append(Node(i[1], i[2]))
            elif i[0] == 1:
                if len(i) != 4:
                    raise ValueError('malformed edge')
                self.edges.append(Edge(i[1], i[2], i[3]))
            elif i[0] == 2:
                if len(i) != 3:
                    raise ValueError('malformed attr')
                self.attrs[i[1]] = i[2]
            else:
                raise ValueError('unknown item')

