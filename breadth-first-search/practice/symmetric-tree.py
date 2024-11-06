from _helper import Helper
from collections import deque

helper = Helper()
TreeNode = helper.TreeNode

class Solution:
    
    # iterative approach: uses O(n) time and O(n) space
    def is_symmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        
        left_node = root.left
        right_node = root.right
        
        # since we want to check if the tree is symetrical, 
        # we want to keep separate queues for the left and
        # right branches so that we can iterate through both
        # and check if the node values at each side are equal
        left_queue = deque([left_node])
        right_queue = deque([right_node])
        
        while left_queue and right_queue:
            
                current_left = left_queue.popleft()
                current_right = right_queue.popleft()
                
                # If only one of them is None, the tree is not symmetric
                if (current_left is None) != (current_right is None):
                    return False
                
                # If both are None, continue to the next iteration
                # to check other nodes in the queues
                if current_left is None and current_right is None:
                    continue
                
                
                if current_left.val != current_right.val:
                    return False
                
                
                left_queue.append(current_left.left)
                left_queue.append(current_left.right)
                
                # add the right of the right branch to the queue first
                # so that it can be compared to the left of the left branch
                # for the symmetrical check
                
                right_queue.append(current_right.right)
                right_queue.append(current_right.left)
                
                    
            
        return True
    
    # iterative approach, but uses a single queue
    def is_symmetric_s(self, root: TreeNode) -> bool:
            if not root:
                return True
            
            queue = deque([(root.left, root.right)])
            
            while queue:
                left, right = queue.popleft()
                
                # If both nodes are None, move to the next pair
                if not left and not right:
                    continue
                
                # If only one of them is None or their values don't match, return False
                if not left or not right or left.val != right.val:
                    return False
                
                # Push the children in symmetric order:
                # left's left with right's right and left's right with right's left
                queue.append((left.left, right.right))
                queue.append((left.right, right.left))
            
            return True
        
    # recursive approach: uses O(n) time, but avoids
    # storing the two queues in memory, hence, reducing
    # space complexity to O(h) where h is the height of the
    # tree and is approximately log(n)
    def is_symmetric_r(self, root:TreeNode) -> bool:
        if not root:
            return True
        
        return self.is_mirror(root.left, root.right)
    
    def is_mirror(self, left: TreeNode, right: TreeNode) -> bool:
        # Base case: both nodes are None
        if not left and not right:
            return True
        # If only one of them is None, return False
        if not left or not right:
            return False
        # Check if values are the same and the children are mirrors
        return (left.val == right.val and 
                self.is_mirror(left.left, right.right) and 
                self.is_mirror(left.right, right.left))
       

    



root = helper.list_to_binary_tree([1,2,2,None,3,None,3])

solution = Solution()
print(solution.is_symmetric(root))
    
