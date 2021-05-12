class TreeNode:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        fmt = 'TreeNode(data={}, left={}, right={})'
        return fmt.format(self.data, self.left, self.right)


class BinarySearchTree:
    def __init__(self, tree_data):
        self.root = TreeNode(tree_data[0])
        for item in tree_data[1:]:
            current = self.root
            while True:
                if int(item) <= int(current.data):
                    if current.left is None:
                        current.left = TreeNode(item)
                        break
                    else:
                        current = current.left
                else:
                    if current.right is None:
                        current.right = TreeNode(item)
                        break
                    else:
                        current = current.right

    def data(self):
        return self.root

    def sorted_data(self):
        result = []
        def inorder(result, node):
            if node is not None:
                inorder(result, node.left)
                result.append(node.data)
                inorder(result, node.right)
        inorder(result, self.root)
        return result

