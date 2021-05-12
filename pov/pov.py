from json import dumps


class Tree:
    def __init__(self, label, children=[]):
        self.label = label
        self.children = children

    def __dict__(self):
        return {self.label: [c.__dict__() for c in sorted(self.children)]}

    def __str__(self, indent=None):
        return dumps(self.__dict__(), indent=indent)

    def __lt__(self, other):
        return self.label < other.label

    def __eq__(self, other):
        return self.__dict__() == other.__dict__()

    def from_pov(self, from_node):
        root = None
        path = self._find_path(from_node)

        while path:
            node = path.pop(0)
            if root:
                root.children.remove(node)
                root = Tree(node.label, node.children + [root])
            else:
                root = Tree(node.label, node.children)
        
        return root

    def path_to(self, from_node, to_node):
        path = self._find_path(to_node, self.from_pov(from_node))
        res = []
        for node in path:
            res.append(node.label)
        return res
            
    def _find_path(self, node, tree=None):
        if tree is None:
            tree = self._deepcopy()

        stack = [[tree]]
        while stack:
            path = stack.pop()
            if path[-1].label == node:
                return path
            
            for child in path[-1].children:
                stack.append(path + [child])

        raise ValueError(f'Node {node} does not exist')

    def _deepcopy(self):
        return Tree(
            self.label, 
            [child._deepcopy() for child in self.children]
        )
