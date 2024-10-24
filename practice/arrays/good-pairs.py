# https://leetcode.com/problems/number-of-good-pairs/description/

class Solution:
    def num_identical_pairs(self, nums: list[int]) -> int:
        freq = {}
        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1
        
        res = 0
        for count in freq.values():
            if count > 1:
                # using the combination formula to get how many pairs of items
                # can be picked from a given count of items
                res += count * (count - 1) // 2  # C(k, 2)

        return res
                
            
            
solution = Solution()

print(solution.num_identical_pairs([1, 2, 3, 1, 1, 3]))

                
        
        