# https://leetcode.com/problems/contains-duplicate

class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        unique_nums = set()

        for num in nums:
            if num in unique_nums:
                return True
            
            unique_nums.add(num)
        
        return False





solution = Solution()
print(solution.containsDuplicate([1,2,3,1]))