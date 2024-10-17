class Solution:
    def search_insert(self, nums: list[int], target: int) -> int:
        low = 0
        high = len(nums) - 1

        while low <= high:
            # as long as there's a range between the low and high position
            # keep searching for the item if it has not been found yet
            # always guess with the new midpoint
            mid = (low + high) // 2
            guess = nums[mid]
            if guess == target:
                return mid
            
            # what we guessed is greater than what we're looking for, so
            # we need to focus on the lower half of the list
            if guess > target:
                high = mid -1
            else:
                # otherwise focus the next search on the higher half of the list
                low = mid + 1

            

        # if the item is not in the list, the last mid position would have
        # gotten close to the item's position as much as possible, so if we were to
        # insert the itme in the list, it that will be at the position 
        # that is one step behind mid, which is low
        return low


solution = Solution()
print(solution.search_insert([1, 3, 5, 7, 9, 11, 13, 15, 21, 24, 30], 18))


# https://leetcode.com/problems/remove-duplicates-from-sorted-array
        