from collections import deque

class Helper():
    def __init__(self):
        pass

    class TreeNode:
        def __init__(self, val=0, left=None, right=None):
            self.val = val
            self.left = left
            self.right = right


    def list_to_binary_tree(self, arr):
        if not arr:
            return None
        
        root = self.TreeNode(arr[0])  # Start with the first element as the root
        
        # The queue keeps track of nodes that have been added to the tree but
        # still need to have their children populated. This allows us to process nodes
        # sequentially from the queue, so that both left and right children
        # are added in level-order (breadth-first) to match the binary tree structure.
        queue = deque([root])
        i = 1
        
        while i < len(arr):
            current = queue.popleft()
            
            # Insert the left child
            if i < len(arr):
                current.left = self.TreeNode(arr[i])
                queue.append(current.left)
                i += 1
            
            # Insert the right child
            if i < len(arr):
                current.right = self.TreeNode(arr[i])
                queue.append(current.right)
                i += 1
        
        return root