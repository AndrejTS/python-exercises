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


def parse(string):
    root = None
    stack = list(string)

    if not stack:
        raise ValueError('.')

    if ''.join(stack[0:2]) != '(;' or stack[-1] != ')':
        raise ValueError('.')

    stack.pop(0)

    def pop_until(char):
        result = ''
        while stack[0] != char:
            result += stack.pop(0)
            if result[-1] == char:
                return result
            if result[-1] == '\\':
                result = result[:-1] + stack.pop(0)
            if not stack:
                raise ValueError('.')
        return result

    def get_properties():
        properties = {}
        while stack[0].isupper():
            key = pop_until('[')
            if not key.isupper():
                raise ValueError('.')
            values = []
            while stack[0] == '[':
                stack.pop(0)
                value = pop_until(']')
                stack.pop(0)
                value = value.replace("\t", " ")
                values.append(value)
            properties[key] = values
        return properties

    def get_nested_tree():
        nested_tree = ''
        while True:
            nested_tree += pop_until(')')
            nested_tree += stack.pop(0)
            if nested_tree.count('(') == nested_tree.count(')'):
                break
        return nested_tree

    while stack:
        if stack[0] != ';':
            raise ValueError('.')
        while stack.pop(0) == ';':
            properties = get_properties()
            node = SgfTree(properties)
            if root is None:
                root = node
                current_node = root
            else:
                current_node.children.append(node)
                current_node = node
            while stack[0] == '(':
                nested_tree = get_nested_tree()
                current_node.children.append(parse(nested_tree))

    return root


# test = parse("(;A[B];B[C];C[D];D[E])")
# print(test.properties)
# print(test.children[0].properties)
# print(test.children[0].children[0].properties)
# print(test.children[0].children[0].children[0].properties)
# print(test.children[0].children[0].children[0].children)


# test = parse(
#     "(;A[B](;B[C][ttt](;P[Z])(;D[Z]E[U];K[L][aaa]))(;C[D]);X[T];Y[U])")
# print(test.properties)
# print(test.children[0].children[1].properties)
# print(test.children[0].children[1].children[0].properties)
# print(test.children[1].properties)
# print(test.children[2].properties)
# print(test.children[2].children[0].properties)
