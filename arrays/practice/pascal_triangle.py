class Solution:


    def generate(self, numRows:int) -> list[list[int]]:
        rows = [[1]]

        while numRows > 1:
            last_row = rows[-1]
            new_row = [1] + [last_row[i]+last_row[i+1] for i in range(len(last_row)-1)] + [1]
            rows.append(new_row)
        
            numRows -= 1
        
        return rows




solution = Solution()
print(solution.generate(5))


#https://leetcode.com/problems/pascals-triangle/
        