class Node():
    def __init__(self, value, parent=None):
        self.value = value
        self.left = None
        self.right = None
        self.parent = parent


class Zipper():
    @staticmethod
    def from_tree(tree):
        return Zipper(tree)

    def __init__(self, tree):
        self.root = self.create_node(tree, parent=None)
        self.focus = self.root

    def create_node(self, tree, parent):
        if tree is None:
            return None
        node = Node(tree['value'], parent)
        if tree['left']:
            node.left = self.create_node(tree['left'], parent=node)
        if tree['right']:
            node.right = self.create_node(tree['right'], parent=node)        
        return node

    def value(self):
        return self.focus.value

    def set_value(self, value):
        self.focus.value = value
        return self

    def left(self):
        if self.focus.left is None:
            return
        self.focus = self.focus.left
        return self

    def set_left(self, tree):
        self.focus.left = self.create_node(tree, self.focus)
        return self

    def right(self):
        if self.focus.right is None:
            return
        self.focus = self.focus.right
        return self

    def set_right(self, tree):
        self.focus.right = self.create_node(tree, self.focus)
        return self

    def up(self):
        if self.focus.parent is None:
            return
        self.focus = self.focus.parent
        return self

    def to_tree(self):
        def traverse(node):
            res = {}
            res['value'] = node.value
            if node.left:
                res['left'] = traverse(node.left)
            else:
                res['left'] = None
            if node.right:
                res['right'] = traverse(node.right)
            else:
                res['right'] = None
            return res
        return traverse(self.root)
