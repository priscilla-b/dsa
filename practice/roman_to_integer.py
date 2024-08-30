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

        if len(s) == 1:
            return r_dict[s]
        
        num = 0
        if len(s) == 2:
            num_1 = r_dict[s[0]]
            num_2 = r_dict[s[1]]
            if num_1 < num_2:
                num = num_2 - 1
            else:
                num = num_1 + num_2
            return num
        
        return num + self.romanToInt(s[1:])


solution = Solution()
print(solution.romanToInt('DCLIX'))