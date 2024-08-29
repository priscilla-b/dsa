
class Solution(object):

    #  naive approach
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        reverse x and check if reversed number and original number are same
        """
        str_x = str(x)
        return str_x[::-1] == str_x
    
    def isPalindromeOpt(self, x):
        # partition x into two and check if each side is equal
        str_x = str(x)
        part_1 = str_x[:len(str_x)//2 +1]
        part_2 = str_x[len(str_x)//2:]
        return  part_1 == part_2
    

solution = Solution()
print(solution.isPalindromeOpt(131))
        
        
    







# source: https://leetcode.com/problems/palindrome-number/