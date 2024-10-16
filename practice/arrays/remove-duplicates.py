class Solution:
    def remove_duplicates(self, nums: list[int]) -> int:

        if not nums:  
            return 0

       # Pointer for the next unique element
        unique_index = 0  # Points to where the next unique element should go

        for i in range(1, len(nums)):  # Start from the second element
            if nums[i] != nums[unique_index]:  # Found a new unique element
                unique_index += 1
                nums[unique_index] = nums[i]  # Place the unique element in its new position

        # The number of unique elements is unique_index + 1
        return unique_index + 1
        
    
   
            


solution = Solution()
print(solution.remove_duplicates([1,1, 1,2,3,3,3,4]))