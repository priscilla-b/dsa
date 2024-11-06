
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
        # partition x into two, reverse one half, and check if it's 
        # equal to the other half
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        
        reversed_half = 0
        while x > reversed_half:
            reversed_half = reversed_half * 10 + x % 10
            x //= 10

        # Step 3: Compare the original number (or its half) with the reversed half
        return x == reversed_half or x == reversed_half // 10

        
    

solution = Solution()
print(solution.isPalindromeOpt(12641))
        
        
    







# source: https://leetcode.com/problems/palindrome-number/