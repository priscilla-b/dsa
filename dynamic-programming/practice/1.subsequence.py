# https://leetcode.com/problems/is-subsequence/

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        m, n = len(s), len(t)

        # create a matrix with m+1 rows and n+1 columns initialized with 0 values
        # added 1 to each length for base cases where either string are empty
        grid = [[0]*(n+1) for _ in range(m+1)]
        
        for i in range(1, m+1):
            for j in range(1, n+1):
                if m[i] == n[j]:
                    grid[i][j]
        
        print(grid)
        
        
solution = Solution()
solution.isSubsequence("abc", "ahbgdc")
        
    
    
