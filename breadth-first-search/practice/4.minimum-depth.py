# https://leetcode.com/problems/minimum-depth-of-binary-tree/

from _helper import Helper
from collections import deque

helper = Helper()
TreeNode = helper.TreeNode


class Solution:
    def min_depth(self, root: TreeNode) -> int:
        # The minimum depth is the number of nodes along the shortest path 
        # from the root node down to the nearest leaf node.

        min_depth = 0
        
        if not root:
            return min_depth
        
        queue = deque([root])
        while queue:
            # start of a level, increment count
            min_depth += 1
            
            # to find min depth, we just need to traverse the tree 
            # and then at each level, check if there's leaf node (a node with no
            # left of right children). The level with the nearest leaf node gives
            # the minimum depth
            level_size = len(queue)
            # process all nodes at the current level
            for _ in range(level_size):
                node = queue.popleft()
                
                # If this node is a leaf node, return the current depth
                if not node.left and not node.right:
                    return min_depth
                
                # Add the left and right children to the queue for the next level
                if node.left:
                    queue.append(node.left)
                                
                if node.right:
                    queue.append(node.right)
 
                
        return min_depth
    

# root = helper.list_to_binary_tree([1, 2, 2, 3, 4, 4, 3, 5, 6, None, None, None, None, None,
                                #    None, None, None, 7, 8, 9, 10, None, None, None, None, 11, 12])
# root = helper.list_to_binary_tree([3,9,20,None,None,15,7])
# root = helper.list_to_binary_tree([2,None,3,None,4,None,5,None,6])

root = helper.list_to_binary_tree([1,2,3,4,None,None,5])
solution = Solution()
print(solution.min_depth(root))
            
            
            
                
            
                
            