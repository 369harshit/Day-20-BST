class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

def findPreSuc(root, key):
    if not root:
        return None, None

    pred = None
    succ = None

    while root:
        if root.val == key:
            # If the key is found
            if root.left:
                # Find the maximum value in the left subtree as predecessor
                pred = findMax(root.left)
            if root.right:
                # Find the minimum value in the right subtree as successor
                succ = findMin(root.right)
            break
        elif root.val > key:
            # If the key is smaller, move to the left subtree
            succ = root
            root = root.left
        else:
            # If the key is larger, move to the right subtree
            pred = root
            root = root.right

    return pred, succ

def findMax(node):
    while node.right:
        node = node.right
    return node

def findMin(node):
    while node.left:
        node = node.left
    return node


# Test the program
root = TreeNode(6)
root.left = TreeNode(4)
root.right = TreeNode(9)
root.left.left = TreeNode(2)
root.left.right = TreeNode(5)
root.right.left = TreeNode(7)
root.right.right = TreeNode(10)

key = 5
predecessor, successor = findPreSuc(root, key)

print("Key:", key)
if predecessor:
    print("Predecessor:", predecessor.val)
else:
    print("Predecessor: None")

if successor:
    print("Successor:", successor.val)
else:
    print("Successor: None")
