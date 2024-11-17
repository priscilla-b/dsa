# https://leetcode.com/problems/is-subsequence/

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        m, n = len(s), len(t)

        # create a matrix with m+1 rows and n+1 columns initialized with 0 values
        # added 1 to each length for base cases where either string are empty
        grid = [[0]*(n+1) for _ in range(m+1)]
        
        for i in range(1, m+1):
            for j in range(1, n+1):
                if s[i-1] == t[j-1]:
                    # if the characters match, increment the value of the 
                    # longest common substring # found so far
                    grid[i][j] = grid[i-1][j-1] + 1
                else:
                    # when characters don't match we have two choices: use the LCS value
                    # before the current s character (grid[i-1][j]) or the one before
                    # the current t character (grig[i][j-1]). taking the higer of those
                    # two values helps to keep the longest subsquence value we have so far
                    grid[i][j] = max(grid[i-1][j], grid[i][j-1])
        
        # if s is a subsequence of t, then the max value of the matrix (last cell value of grid)
        # must be the same length as the length of s (m)
        return grid[m][n] == m
        
        
solution = Solution()
print(solution.isSubsequence("", ""))
        
    
    
