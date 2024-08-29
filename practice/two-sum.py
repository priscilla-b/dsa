class Solution(object):

    # o(n^2) time  complexity
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]

        Returns the indexes of the two elements that add up to the 
        given target number
        """
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if (nums[i] + nums[j]) == target:
                    return [i, j]

    # o(n) time complexity
    def twoSumOpt(self, nums, target):
        """
        Since a number must be added to another to get a target, each number
        has a complement. The idea is to iterate through each element of the 
        array while checking if it's complement exists in the hash map. If not, the
        new element is added to the hash map. Since the function expects the indices of
        the elements to be returned, they are used as the dictionary values.
        """
        map_ = dict()
        for i in range(len(nums)):

            j = map_.get(target - nums[i])
            if j is not None:
                return [j, i]
            else:
                map_[nums[i]] = i
                

   
      


solution = Solution()
# print(solution.twoSum([3, 2, 4], 6))
# print(solution.twoSum([2, 7, 11, 15], 9))
# print(solution.twoSum([3, 3], 6))

print(solution.twoSumOpt([3, 2, 11, 7, 15], 9))


# source: https://leetcode.com/problems/two-sum/description/