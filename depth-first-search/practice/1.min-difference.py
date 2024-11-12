# https://leetcode.com/problems/sum-of-left-leaves/
from collections import deque
from _helper import Helper

TreeNode = Helper.TreeNode

class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        """The most efficient approach to this problem will be using an in-order traversal
        in a DFS approach since this is a binary search tree and values are sorted.
        For a BFS approach, since you can only visit nodes level by level, we have to 
        collect all the node values in a list, then sort it, and find the minimum
        difference between the sorted values

        """
        prev = None # holds the previous node's value in sorted order
        min_diff = float('inf')  # Set an initial large minimum difference
        
        
        def in_order(node):
            nonlocal prev, min_diff
            
            if not node:
                return 

            in_order(node.left)
                
            # Update the minimum difference if `prev` is set
            if prev is not None:
                min_diff = min(min_diff, node.val - prev)
                
            prev = node.val
                
            in_order(node.right)
        
        in_order(root)         
        
        return min_diff
    
helper = Helper()
solution = Solution()
# root = helper.list_to_binary_tree([1,0,48,None,None,12,49])
# root = helper.list_to_binary_tree([1,None,5,3])
root = helper.list_to_binary_tree([22,12,30,8,20,25,40])

print(solution.getMinimumDifference(root))

                
        
