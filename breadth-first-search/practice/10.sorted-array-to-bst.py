
from collections import deque
from _helper import Helper

TreeNode = Helper.TreeNode


class Solution:
    def sorted_array_to_bst(self, nums: list[int]) -> TreeNode:
        # since a bst has nodes at the left lower than the root, 
        # and nodes at the right higher than the root,
        # the root of the node should then come from the middle
        # of a sorted array
        
        if not nums:
            return 
        
        mid_i = len(nums)//2
        
        root = TreeNode(nums[mid_i])
        
        if mid_i == 0:
            return root
        
        left = self.sorted_array_to_bst(nums[:mid_i])
        right = self.sorted_array_to_bst(nums[mid_i:])
        
        root.left = left
        root.right = right
        
        return root
    

helper = Helper()
solution = Solution()
bst = solution.sorted_array_to_bst([-10, -3, 0, 9, 5])
print(helper.binary_tree_to_list(bst))
       
        
        
        
        
        
            
        