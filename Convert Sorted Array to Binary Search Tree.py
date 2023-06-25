from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def sortedArrayToBST(nums):
    if not nums:
        return None

    mid = len(nums) // 2

    root = TreeNode(nums[mid])
    root.left = sortedArrayToBST(nums[:mid])
    root.right = sortedArrayToBST(nums[mid + 1:])

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

nums = [-10,-3,0,5,9]
bst = sortedArrayToBST(nums)
levelOrderTraversal(bst)
