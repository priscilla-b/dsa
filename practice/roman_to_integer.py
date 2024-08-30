class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """

        r_dict = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        return self.helper(s, r_dict)      

    def helper(self, s, r_dict):

        if len(s) == 0:
            return 0
        
        num = r_dict[s[0]]
        if len(s) == 1:
            return num
    
        num_2 = r_dict[s[1]]
        if num < num_2:
            # when there's a subtraction situation, treat the two numbers
            # as one and add the result of their subraction to the final number
            # since the two numbers are treated as one, they should both be skipped
            return num_2 - num + self.helper(s[2:], r_dict)
        else:
            return num + self.helper(s[1:], r_dict)

        
        



solution = Solution()
# print(solution.romanToInt('DCLIX'))
# print(solution.romanToInt('CLVIII'))
print(solution.romanToInt('MCMXCIV'))

