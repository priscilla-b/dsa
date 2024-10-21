# https://leetcode.com/problems/intersection-of-two-arrays/

class Solution:
    """
    Idea is to return the unique elements that exist in both lists
    regardless of position
    """
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        common = set()
        nums1_set = set(nums1)
        for num in nums2:
            if num in nums1_set:
                common.add(num)
       
        
        return [num for num in common]
    

solution = Solution()
print(solution.intersection([1,2,2,4], [2, 2]))
        