# https://leetcode.com/problems/two-sum
class Solution(object):
    # brute force solution: O(n^2) time complexity, O(1) space complexity
    def twoSum_bf(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            # initialize j to be the next index after i, so we don't check the same pair twice
            for j in range( i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        # len() is O(1) in python because it is stored as a property of the list object
        
    
    def twoSum(self, nums, target):
        
        """
        My solution using a hash map to store the complements of the numbers we have seen so far.
        Trades off time complexity for space complexity. O(n) time complexity, O(n) space complexity
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        complements = {}
        for i in range(len(nums)): 
            # check if current number exists in dictionary beforeadding its complement 
            # to the dictionary. this avoids checking the same number twice, which would be 
            # incorrect if the target is twice that number (e.g., target=4, nums=[2, 2])
            if nums[i] in complements:
                return [complements[nums[i]], i]
            complements[target - nums[i]] = i
            
        # return an empty list if no solution is found
        return []
    
    def twoSum2(self, nums, target):
        """
        Standard solution using a hash map to store the numbers we have seen so far.
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        seen = {}
        for i, num in enumerate(nums):
            if num in seen:
                return [seen[num], i]
            seen[target - num] = i
            
        # return an empty list if no solution is found
        return []
        
Solution = Solution()
print(Solution.twoSum([2, 7, 11, 15], 3)) # [0, 1]