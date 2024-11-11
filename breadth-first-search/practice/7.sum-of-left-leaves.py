# https://leetcode.com/problems/sum-of-left-leaves/
from collections import deque
from _helper import Helper

TreeNode = Helper.TreeNode

class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        leaf_sum = 0
        if not root:
            return leaf_sum
        
        queue = deque([root])
        
        while queue:
            current = queue.popleft()
            if current.left:
                # if the left node is a leaf node,then add it's value
                # to the sum of leaf node values
                if not current.left.left and not current.left.right:
                    leaf_sum+=current.left.val
                queue.append(current.left)
                
            if current.right:
                queue.append(current.right)

        return leaf_sum
    
    
helper = Helper()
solution = Solution()
root = helper.list_to_binary_tree([3,9,20,None,None,15,7])

print(solution.sumOfLeftLeaves(root))

                
        
