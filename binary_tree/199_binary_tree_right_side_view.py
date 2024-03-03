"""
199. Binary Tree Right Side View

Medium

Given the root of a binary tree, imagine yourself standing on the right side of 
it, return the values of the nodes you can see ordered from top to bottom.
"""

from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def rightSideView(root):
    q = deque([])
    level = 0 
    right_side = []

    if root is None:
        return []
    
    #right_side = {
    #    level : root.val
    #}

    q.appendleft(root)

    while q:
        current = q.pop()
        if level ==len(right_side):
            right_side.append(current.val)

        if current.right != None:
            q.appendleft(current.right)

        if current.left != None:
            q.appendleft(current.left)
    
    return right_side