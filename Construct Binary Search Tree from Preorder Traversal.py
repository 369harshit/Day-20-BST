from collections import deque
class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

def constructBST(preorder):
    if not preorder:
        return None

    root = TreeNode(preorder[0])

    for i in range(1, len(preorder)):
        insert(root, preorder[i])

    return root

def insert(root, value):
    if not root:
        return TreeNode(value)

    if value < root.val:
        root.left = insert(root.left, value)
    else:
        root.right = insert(root.right, value)

    return root

def levelOrderTraversal(root):
    if not root:
        return

    queue = deque([root])

    while queue:
        node = queue.popleft()
        print(node.val, end=' ')

        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)


# Test the program
preorder = [8, 5, 1, 7, 10, 12]
root = constructBST(preorder)
levelOrderTraversal(root)
