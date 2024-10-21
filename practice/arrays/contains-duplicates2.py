# https://leetcode.com/problems/contains-duplicate-ii


class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        """
        The idea is to iterate through the list and keep a hashmap of each 
        number and its position. if a number already exists in the hashmap,
        then it has a duplicate. so fetch the position of its duplicate and 
        check if the difference in positions of the duplicate is less or equal to k.
        """
        seen = {}

        for i in range(len(nums)):
            if nums[i] in seen.keys():
                j = seen[nums[i]]
                if abs(i-j) <= k:
                    return True
                else:
                    seen[nums[i]] = i
                    
            else:

                seen[nums[i]] = i
        
        return False
            
        




solution = Solution()
print(solution.containsNearbyDuplicate([1,2,3,1], 3))
print(solution.containsNearbyDuplicate([1,2,3,1, 2, 3], 2))
print(solution.containsNearbyDuplicate([1,0,1,1], 1))
print(solution.containsNearbyDuplicate([99,99], 2))