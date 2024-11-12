# Depth-First Search

Involves traversing a binary tree by exploring as far down one branch as possible, before backtracking to explore other branches.

Common DFS traversal methods include:
- In-order (Left, Root, Right)
- Pre-order (Root, Left, Right)
- Post-order (Left, Right, Root)

```py
# Inorder Traversal
class TreeNode:
    def __init__(self, v):
        self.left = None
        self.right = None
        self.val = v

def printInorder(root):
    if root:
        # Traverse left subtree
        printInorder(root.left)
        
        # Visit node
        print(root.val,end=" ")
        
        # Traverse right subtree
        printInorder(root.right)
