# https://leetcode.com/problems/maximum-depth-of-binary-tree

from _helper import Helper
from collections import deque

helper = Helper()
TreeNode = helper.TreeNode


class Solution:
    def max_depth(self, root: TreeNode) -> int:
        # A binary tree's maximum depth is the number of nodes along 
        # the longest path from the root node down to the farthest leaf node.
        max_depth = 0
        
        if not root:
            return max_depth
        
        queue = deque([root])
        while queue:
            # start of a level, increment count
            max_depth += 1
            
            # to find max depth, we just need to count the number of
            # levels of nodes in the tree
            
            level_size = len(queue)
            # process all nodes at the current level
            for _ in range(level_size):
                node = queue.popleft()
                
                # Add the left and right children to the queue for the next level
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
           
                
        return max_depth
    

root = helper.list_to_binary_tree([1, 2, 2, 3, 4, 4, 3, 5, 6, None, None, None, None, None,
                                   None, None, None, 7, 8, 9, 10, None, None, None, None, 11, 12])

solution = Solution()
print(solution.max_depth(root))
            
            
            
                
            
                
            