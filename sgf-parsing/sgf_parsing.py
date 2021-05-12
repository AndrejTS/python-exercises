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


NODE = ';'
TREE_START = '('
TREE_END = ')'
VALUE_START = '['
VALUE_END = ']'


def parse(string):
    if string[0:2] != "(;" or string[-1] != ")":
        raise ValueError("Input String Invalid")
    # current string index
    global index
    index = 0
    return parse_tree(string)


def parse_tree(string):
    global index
    root = cur_node = None
    
    while string[index] != TREE_END:
        if string[index] == TREE_START:
            index += 1
            if root is None:
                index += 1
                properties = parse_node(string)
                node = SgfTree(properties)
                root = cur_node = node
            else:
                cur_node.children.append(parse_tree(string))
        else:
            index += 1
            properties = parse_node(string)
            node = SgfTree(properties)
            if root is None:
                root = node
            else:
                cur_node.children.append(node)
            cur_node = node

    index += 1
    return root


def parse_node(string):
    properties = {}

    while string[index] not in [NODE, TREE_START, TREE_END]: 
        try:
            key, values = parse_property(string)
        except IndexError:
            raise ValueError("Invalid property")
        properties[key] = values

    return properties


def parse_property(string):
    global index
    key = ""
    values = []

    while string[index] != VALUE_START:
        key += string[index]
        index += 1

    if not key.isupper():
        raise ValueError(f"Invalid key: {key!r}")

    while string[index] == VALUE_START:
        value = parse_value(string)
        values.append(value)

    return key, values


def parse_value(string):
    global index
    index += 1
    value = ''

    while string[index] != VALUE_END or value.endswith("\\"):
        value += string[index]
        index += 1

    index += 1
    value = value.replace("\\]", "]").replace("\t", " ")
    return value



# test = parse("(;A[B];B[C];C[D];D[E])")
# print(test.properties)
# print(test.children[0].properties)
# print(test.children[0].children[0].properties)
# print(test.children[0].children[0].children[0].properties)
# print(test.children[0].children[0].children[0].children)


# test = parse("(;A[B](;B[C][ttt](;P[Z])(;D[Z]E[U];K[L][aaa]))(;C[D]);X[T];Y[U])")
# print(test.properties)
# print(test.children[0].children[1].properties)
# print(test.children[0].children[1].children[0].properties)
# print(test.children[1].properties)
# print(test.children[2].properties)
# print(test.children[2].children[0].properties)

