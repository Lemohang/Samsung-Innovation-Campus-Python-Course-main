class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def tree_depth(node):
        if node is None:
            return 0
        return 1 + max(tree_depth(node.left), tree_depth(node.right))

root = Node(4)
root.left = Node(2)
root.right = Node(6)
root.left.left = Node(1)
root.left.right = Node(3)
root.right.left = Node(5)
root.right.right = Node(7)

print(tree_depth(root))

