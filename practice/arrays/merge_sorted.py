class Solution:

    # using two-pointer approach
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Merge nums2 into nums1 in-place while maintaining sorted order.
        """
        # Start merging from the end of nums1
        last = m + n - 1  # Last index of nums1
        m -= 1  # Last index of the elements in nums1
        n -= 1  # Last index of the elements in nums2

        # While there are elements in both arrays
        while m >= 0 and n >= 0:
            if nums1[m] > nums2[n]:
                nums1[last] = nums1[m]  # Place nums1[m] in the last position
                m -= 1  # Move pointer in nums1
            else:
                nums1[last] = nums2[n]  # Place nums2[n] in the last position
                n -= 1  # Move pointer in nums2
            last -= 1  # Move the last position pointer

        # If there are any remaining elements in nums2, place them in nums1
        while n >= 0:
            nums1[last] = nums2[n]
            n -= 1
            last -= 1

        # return nums1


    def merge1(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        # Copy nums2 elements into nums1 starting from index m
        for i in range(m, m+n):
            nums1[i] = nums2[i-m]

            # Sort the array from index 0 to i  after each insertion
            self.insert_sorted(nums1, i)

        # return nums1
    
    def insert_sorted(self, nums, index):
        """
        Insert the element at nums[index] into its correct position in the sorted portion nums[0:index].
        """
        num_to_insert = nums[index]  
        i = index  # Start from the current index of the number to insert

        # Move elements to the right to make space for the new element
        while i > 0 and nums[i - 1] > num_to_insert:
            nums[i] = nums[i - 1]  # Shift larger element to the right
            i -= 1  

        # Place the new element at its correct position
        nums[i] = num_to_insert



      


   



solution = Solution()
print(solution.merge([4, 5, 6, 0, 0, 0], 3, [1, 2, 3], 3))


#https://leetcode.com/problems/merge-sorted-array
        