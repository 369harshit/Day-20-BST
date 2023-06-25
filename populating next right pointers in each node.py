class Node:
    def __init__(self, val, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

def connect(root):
    if not root:
        return root

    if root.left:
        root.left.next = root.right
        if root.next:
            root.right.next = root.next.left

    connect(root.left)
    connect(root.right)

    return root

def printTree(root):
    if not root:
        return

    result = []
    while root:
        current = root
        while current:
            result.append(current.val)
            current = current.next
        result.append('#')
        root = root.left

    print(result)

# Test the program
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

connect(root)
printTree(root)
