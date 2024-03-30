class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def inorder(root):
    left = inorder(root.left) if root else []
    root_ = [root.val] if root else []
    right = inorder(root.right) if root else []
    
    return left + root_ + right 

one = TreeNode(1)
two = TreeNode(2)
three = TreeNode(3)

one.right = two
two.left = three

print(inorder(one))
        