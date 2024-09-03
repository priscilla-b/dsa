class Solution(object):

    # naive solution
    def getLucky(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """

        digits = ''
        for char in s:
            digits += f'{ord(char) - 96}'  #unicode codes start at 97 for the alphabets

        t = 1 #number of transformations to be done
        while t <= k:
            digits_t = 0
            for num in digits:
                digits_t += int(num)

                digits = str(digits_t)

            t+=1
            
    
        return int(digits)


solution = Solution ()
print(solution.getLucky('iiii', 1))





# source: https://leetcode.com/problems/sum-of-digits-of-string-after-convert/