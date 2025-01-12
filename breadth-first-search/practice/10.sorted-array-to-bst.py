
from collections import deque
from _helper import Helper

TreeNode = Helper.TreeNode


class Solution:
    def sorted_Array_ToBST(self, nums: list[int]) -> TreeNode:
        root = TreeNode(nums[0])
        current = root
        
        for num in nums[1:]:
            if num > current:
                current.right = num
            else:
                current.left = num
            
            current = root.left
        