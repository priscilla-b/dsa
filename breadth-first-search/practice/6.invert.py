# https://leetcode.com/problems/invert-binary-tree/
from collections import deque
from _helper import Helper

TreeNode = Helper.TreeNode

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        queue = deque([root])
        if not root:
            return root
        while queue:
            current = queue.popleft()
            
            current.left, current.right = current.right, current.left
            
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)

            
        return root


helper = Helper()
solution = Solution()
root = helper.list_to_binary_tree([4,2,7,1,3,6,9])

solution.invertTree(root)
