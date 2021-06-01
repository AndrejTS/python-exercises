class SgfTree:
    def __init__(self, properties=None, children=None):
        self.properties = properties or {}
        self.children = children or []

    def __eq__(self, other):
        if not isinstance(other, SgfTree):
            return False
        for k, v in self.properties.items():
            if k not in other.properties:
                return False
            if other.properties[k] != v:
                return False
        for k in other.properties.keys():
            if k not in self.properties:
                return False
        if len(self.children) != len(other.children):
            return False
        for a, b in zip(self.children, other.children):
            if a != b:
                return False
        return True

    def __ne__(self, other):
        return not self == other


class Parser:
    def __init__(self, string):
        self.stack = list(string)

    def pop_until(self, char):
        # e.g. stack = FF[4];B[aa]
        # pop_until('[')
        # result -> FF, stack -> [4];B[aa]
        result = ''
        while self.stack[0] != char:
            result += self.stack.pop(0)
            if result[-1] == '\\':
                result = result[:-1] + self.stack.pop(0)
            if not self.stack:
                raise ValueError('Syntax error')
        return result

    def get_properties(self):
        properties = {}
        while self.stack:
            # if next char indicate new node or nested tree => break
            if self.stack[0] in '(;':
                break
            key = self.pop_until('[')
            if not key.isupper():
                raise ValueError('Syntax error')
            values = []
            while self.stack:
                # if no more values => break
                if self.stack[0] != '[':
                    break
                self.stack.pop(0)
                value = self.pop_until(']')
                self.stack.pop(0)
                value = value.replace("\t", " ")
                values.append(value)
            properties[key] = values
        return properties

    def get_nested_tree(self):
        # (;A[1];B[2])(;C[3];D[4]) => (;A[1];B[2])
        # (;A[1](;B[2]))(C[3]) => (;A[1](;B[2]))
        nested_tree = ''
        while self.stack:
            nested_tree += self.pop_until(')')
            nested_tree += self.stack.pop(0)
            if nested_tree.count('(') == nested_tree.count(')'):
                break
        return nested_tree

    def parse(self):
        root = None

        if not self.stack:
            raise ValueError('Empty string')

        if self.stack.pop(0) != '(' or self.stack.pop() != ')':
            raise ValueError('Syntax error')

        # parse nodes and possible nested trees
        while self.stack:
            # node must start with ';
            if self.stack.pop(0) != ';':
                break
            properties = self.get_properties()
            node = SgfTree(properties)
            if root is None:
                root = node
                current_node = root
            else:
                current_node.children.append(node)
                current_node = node
            # check for nested trees
            while self.stack:
                if self.stack[0] != '(':
                    break
                nested_tree = self.get_nested_tree()
                parsed_nested_tree = Parser(nested_tree).parse()
                current_node.children.append(parsed_nested_tree)

        # at the end, stack must be empty and root must not be None
        if self.stack or (root == None):
            raise ValueError('Syntax error')

        return root


def parse(string):
    return Parser(string).parse()
