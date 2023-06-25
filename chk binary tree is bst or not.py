class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def is_valid_bst(root):
    # Helper function for in-order traversal
    def inorder(node, values):
        if node:
            inorder(node.left, values)
            values.append(node.val)
            inorder(node.right, values)

    # Perform in-order traversal and store the values
    values = []
    inorder(root, values)

    # Check if the values are in ascending order
    for i in range(1, len(values)):
        if values[i] <= values[i - 1]:
            return False

    return True

# Example tree: [2, 1, 3]
root = TreeNode(2)
root.left = TreeNode(1)
root.right = TreeNode(3)

print(is_valid_bst(root))  # Output: True

# Example tree: [5, 1, 4, null, null, 3, 6]
root = TreeNode(5)
root.left = TreeNode(1)
root.right = TreeNode(4)
root.right.left = TreeNode(3)
root.right.right = TreeNode(6)

print(is_valid_bst(root))  # Output: False
