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
        if not root:
            return 0
        
        # Step 1: Perform BFS and collect all node values
        queue = deque([root])
        values = []
        
        while queue:
            current = queue.popleft()
            values.append(current.val)
            
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
        
        # Step 2: Sort the values
        values.sort()
        
        # Step 3: Find the minimum difference between adjacent values
        min_diff = float('inf')
        for i in range(1, len(values)):
            min_diff = min(min_diff, values[i] - values[i - 1])
        
        return min_diff    
    
helper = Helper()
solution = Solution()
# root = helper.list_to_binary_tree([1,0,48,None,None,12,49])
root = helper.list_to_binary_tree([1,None,5,3])

print(solution.getMinimumDifference(root))

                
        
