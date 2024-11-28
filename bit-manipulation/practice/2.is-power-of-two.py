class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        """
        Using modular and integer division approach
        
        """
        n = abs(n)
        if n == 0:
            return False
        if n == 1:
            return True
        
        while n > 1:
            if n % 2 != 0:
                return False
            n = n // 2
            
            
        return True
    
    def isPowerOfTwo(self, n: int) -> bool:
        """
        Using the bitwise approach.
        Any number that's a power of two has just one bit set to 1.
        Starting at 2^0 = 0001, 2^1 will add one bit to the right (shift left)
        evaluating to 2^1 = 0010, 2^2(4) = 0100, 2^3(8) = 1000 and so on.
        Any increment in exponent just adds one 0 to the right of the binary
        representation of the number, and that's why a number which is a power of
        two has just one bit set to 1.
        
        To check if a number is a power of two, we just need to check if it has
        only one bit set to 1.
        We do this by performing a binary subtraction (n-1). If the number is a power of 2, 
        the binary subtraction will flip the the bits of n (turn the first 1 to 0 and all the 0s to 1, 
        hence creating a complement of n). e.g.: 1000 (8) - 1 = 0111 (7)
        Performing a bitwise & operation between n and its complement i.e. n&(n-1) should then result in 0.
        If n is not a power of 2, then n-1 in binary terms will not result in the flipped(comlement) of n
        and so n&(n-1) will not return 0.
        
        
        
        """
        # n should be a non-negative integer greater than 0
        return n>0 and n&(n-1) == 0
    
        

solution = Solution()
print(solution.isPowerOfTwo(16))