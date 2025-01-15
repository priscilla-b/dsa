
from collections import deque
from _helper import Helper

TreeNode = Helper.TreeNode


class Solution:
    def sorted_array_to_bst(self, nums: list[int]) -> TreeNode:
        # since a bst has nodes at the left lower than the root, 
        # and nodes at the right higher than the root,
        # the root of the node should then come from the middle
        # of a sorted array
        
        mid_i = len(nums)//2
        
        root = TreeNode(nums[mid_i])
        current = root
        
        # current.left = 
        # create_tree(nums[1:], current.left)
        
        # def create_tree(nums, node):
        #     current.val = nums[0]
        #     return current
        
        
        
        
            
        