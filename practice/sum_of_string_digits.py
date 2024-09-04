class Solution(object):

    # naive solution
    def getLucky(self, s: str, k: int) -> int:

        digits = ''
        for char in s:
            digits += f'{ord(char) - 96}'  #unicode codes start at 97 for the alphabets

        while k > 0:
            digits_t = 0
            for num in digits:
                digits_t += int(num)

                digits = str(digits_t)

            k-=1
            
    
        return int(digits)


    # optimized solution
    def getLuckyOpt(self, s: str, k: int) -> int:

        sum_digits = 0
        for char in s:
            digits = (ord(char) - 96)
            while digits > 0:
                # add each number in digits to the
                # total number to be returned
                sum_digits += digits % 10
                digits //= 10
          

        while k > 1:
            digits_t = 0
            while sum_digits > 0:
                digits_t += sum_digits % 10
                sum_digits //= 10
                
            sum_digits = digits_t
            k -= 1
            
    
        return sum_digits


solution = Solution ()
print(solution.getLuckyOpt('leetcode', 2))





# source: https://leetcode.com/problems/sum-of-digits-of-string-after-convert/