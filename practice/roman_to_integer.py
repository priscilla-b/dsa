class Solution(object):
    
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        This method has an O(n^2) time complexity.
        There are O(n) recursive calls, and
        Each recursive call involves a string slice that also
        take O(n) time complexity
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

    
    def roman_to_int(self, s):
        """
        Using simple iteration
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

        num = 0
        for i in range(len(s)-1):
            first = r_dict[s[i]]
            if len(s) == 1:
                return first
       
            if first < r_dict[s[i+1]]:
                num -= first
            else:
                num += first

        #   add the last number to the final result since it was not included 
        # in the iteration
        return num + r_dict[s[-1]]

    def roman_to_int2(self, s):
        """
        Using a for .. in for iteration
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

        num = 0
        # keep track of the previous number outside the loop
        # so that it can be compared to the current number
        # whenever a new loop starts
        prev_num = 0
        # work with the string backwards
        for char in s[::-1]:
            current_num = r_dict[char]
            if current_num >= prev_num:
                num += current_num
               
            else:
                num -= current_num
            
            # update the value of the previous number 
            # before new loop starts
            prev_num = current_num
        
        return num
         

            

        


        



solution = Solution()
# print(solution.romanToInt('DCLIX'))
# print(solution.romanToInt('CLVIII'))
# print(solution.romanToInt('MCMXCIV'))
print(solution.roman_to_int2('LVIII'))
    



