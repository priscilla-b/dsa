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
        

solution = Solution()
print(solution.isPowerOfTwo(11))