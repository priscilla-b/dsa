# https://leetcode.com/problems/path-sum/description/

from collections import deque
from _helper import Helper


TreeNode = Helper.TreeNode

class Solution:
    def has_path_sum(self, root:TreeNode, targetSum:int) -> bool:
        """
        The goal is to check if the tree has any leaf node, such that the sum of all values
        following a path from the root to that leaf node adds up to the target sum.
        My approach is to traverse the tree, and then update the value of each node, by adding it's
        accumulated value from the root.
        By the time I get to a leaf node, I should have the total path value from root, and so I can 
        check if it's equal to the target sum
        """
        if not root:
            return False
        
        queue = deque([root])

        while queue:
            current = queue.popleft()
            
            # current is a leaf node and its value equals to the target value,
            # then tree has the desired path sum
            if current.val == targetSum and not current.left and not current.right:
                return True
           
            if current.left:
                current.left.val += current.val
                queue.append(current.left)
                    
            if current.right:
                current.right.val += current.val
                queue.append(current.right)
                
        return False
                










helper = Helper()
solution = Solution()

root = helper.list_to_binary_tree([5,4,8,11,None,13,4,7,2,None,None,None,1])
print(solution.has_path_sum(root, 22))

root = helper.list_to_binary_tree([1,2,3])
print(solution.has_path_sum(root, 5))


root = helper.list_to_binary_tree([0,1,1])
print(solution.has_path_sum(root, 1))

