# https://leetcode.com/problems/intersection-of-two-arrays-ii/

class Solution:
    """
    The goal is to find the elements that are common between both lists. If an element appears 
    multiple timesin both lists, it should be included in the result as many times as it appears in both lists.
    
    The challenge is when an element appears more times in one list than the other. In this case, 
    the intersection should only include the element as many times as it appears in both lists.
    
    The solution uses a dictionary to track the frequency of each element in the first list (nums1).
    Then, it loops over the second list (nums2) and checks for the element's existence in the dictionary.
    If the element is found and its count is greater than zero, it is added to the result, 
    and its count is decremented.
    """
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        common = []
        count_dict = {}
        
        for num in nums1:
            if num not in count_dict:
                count_dict[num] = 1
            else:
                count_dict[num] += 1
                
        
        for num in nums2:
            if num in count_dict and count_dict[num] > 0:
                common.append(num)
                count_dict[num] -= 1
            
        
        return common
    

solution = Solution()
print(solution.intersection([1,2] , [1,1]))
        