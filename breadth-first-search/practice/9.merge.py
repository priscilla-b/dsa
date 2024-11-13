# https://leetcode.com/problems/merge-two-binary-trees/
from collections import deque
from _helper import Helper

TreeNode = Helper.TreeNode

class Solution:
    def mergeTrees(self, root1: TreeNode, root2: TreeNode) -> TreeNode:
        """
        
        """
        if not root1:
            return root2
        if not root2:
            return root1
         
        queue1 = deque([root1])
        queue2 = deque([root2])
       
        
        while queue1 and queue2:
            current1 = queue1.popleft()
            current2 = queue2.popleft()
            
            current1.val += current2.val
            
            if current1.left and current2.left: 
                queue1.append(current1.left)
                queue2.append(current2.left)
            elif not current1.left and current2.left:
                current1.left = current2.left
                # Attach the remaining subtree from `current2` to `current1`
                # this will ensure that root1 will have the same 
                # number nodes as root2 for processing
            
   
            if current1.right and current2.right: 
                queue1.append(current1.right)
                queue2.append(current2.right)
                
            elif not current1.right and current2.right:
                current1.right = current2.right
                
        
        
        return root1
    
helper = Helper()
solution = Solution()

root1 = helper.list_to_binary_tree([1,3,2,5])
root2 = helper.list_to_binary_tree([2,1,3,None,4,None,7])

merged = solution.mergeTrees(root1, root2)
print(helper.binary_tree_to_list(merged))

                
        
