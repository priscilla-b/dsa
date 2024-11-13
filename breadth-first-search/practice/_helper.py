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
                if arr[i] is not None:
                    current.left = self.TreeNode(arr[i])
                    queue.append(current.left)
                i += 1
            
            # Insert the right child
            if i < len(arr):
                if arr[i] is not None:
                    current.right = self.TreeNode(arr[i])
                    queue.append(current.right)
                i += 1
            
        return root
    
    
    def binary_tree_to_list(self, root:TreeNode):
        if not root:
            return []
         
        values = [root.val]
        queue = deque([root])
 
        while queue:
            current = queue.popleft()
            if current.left:
                values.append(current.left.val)
                queue.append(current.left)
            else:
                values.append(None)
                
            if current.right:
                values.append(current.right.val)
                queue.append(current.right)
            else:
                values.append(None)
        
         # Remove trailing None values
        while values and values[-1] is None:
            values.pop()
            
        return values
    
            