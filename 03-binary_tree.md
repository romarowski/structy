## Binary Tree

### Tree height problem

**Statement**: Given a binary tree, find its height.

**Approach**: Transverse the tree, keeping track of the height of the left and right subtrees. Return the maximum height.
1. Base case: empty (or null) tree has height -1.
2. Recursive case: return 1 + the maximum height of the left and right subtrees.


```python
def height(node):

    # empty tree
    if node is None:
        return -1
    
    # recursive case
    return 1 + max(height(node.left), height(node.right))
```

**Complexity**:
- Time: O($n$), need to transverse every node on the tree.
- Space: O($n$), we have n calls to ```height()```.


