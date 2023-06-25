class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def search_bst(root, val):
    if not root or root.val == val:
        return root
    
    if val < root.val:
        return search_bst(root.left, val)
    else:
        return search_bst(root.right, val)

# Example BST: [4, 2, 7, 1, 3]
root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(7)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)

val = 2
result = search_bst(root, val)

if result:
    print("Subtree rooted at node with value", val, "exists:")
    print("Value:", result.val)
    if result.left:
       print("Left Child:", result.left.val) 
    else:
        None
        
    if result.right:
       print("Right Child:", result.right.val) 
    else:
        None
        
else:
    print("Subtree rooted at node with value", val, "does not exist.")
