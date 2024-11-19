class Solution:
    def countBits(self, n: int) -> list[int]:
        
        dp = [0]*(n+1)
        
        for i in range(1, n+1):
            dp[i] = dp[i >> 1] + (i&1)

        return dp
        
    
        
        
    
    
solution = Solution()
print(solution.countBits(5))
        
        
       