# https://leetcode.com/problems/fibonacci-number/
class Solution:
    def fib(self, n: int) -> int:
        """
        For a fibonacci sequence, at any point in time, the current number n
        is the sum of the previous two numbers, (n-1) and (n-2)

        
        """
        if n == 0:
            return 0
        
        if n == 1:
            return 1
        
        prev1 = 1
        prev2 = 0
        for _ in range(2, n+1):
            current = prev1 + prev2
            prev2 = prev1
            prev1 = current
            
        return prev1
    
    
solution = Solution()
print(solution.fib(4))
            
            