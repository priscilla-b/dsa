from _helper import Helper
from collections import deque

helper = Helper()
TreeNode = helper.TreeNode

class Solution:
    def is_same_tree(self, p: TreeNode, q: TreeNode) -> bool:
        
        # deque(pronounced deck) is a double-ended queue that enables quick inserts and deletes
        # at both ends of the queue. this will enable us to traverse
        # a node and its left and right more efficiently
        queue_p = deque([p])
        queue_q = deque([q])
        
        while queue_p and queue_q:

            current_p = queue_p.popleft()
            current_q = queue_q.popleft()
            
            if not current_p and not current_q:
                return True
            
            if not current_p or not current_q:
                return False
            
            
            if current_p and current_p.val != current_q.val:
                return False
            
         
            if current_p.left or current_q.left:   
                queue_p.append(current_p.left)
                queue_q.append(current_q.left)
            
    
            if current_p.right or current_q.right:  
                queue_p.append(current_p.right)
                queue_q.append(current_q.right)
            

        return True
            
       
        
       




p = helper.list_to_binary_tree([1, 2, 3])
q = helper.list_to_binary_tree([1, 2, 3])

solution = Solution()
print(solution.is_same_tree(p, q))
    
