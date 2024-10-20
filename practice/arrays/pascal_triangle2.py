
#https://leetcode.com/problems/pascals-triangle-ii/

class Solution:


    def get_row(self, rowIndex:int) -> list[int]:
        last_row = [1]

        while rowIndex > 0:

            new_row = [1] + [last_row[i]+last_row[i+1] for i in range(len(last_row)-1)] + [1]

            last_row = new_row

            rowIndex -= 1
        
        return last_row




solution = Solution()
print(solution.get_row(3))


        