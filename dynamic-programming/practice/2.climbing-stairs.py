
# https://leetcode.com/problems/climbing-stairs

class Solution:
    def climbStairs(self, n: int) -> int:
        """At any point in time, you can only take 1 or 2 steps at a time.
        So say you're currently at step 0 on your staircase and you want to take
        4 steps in total, you can take 1 step to step 1 or 2 steps to step 2.
        At step 1, you can take 1 step to step 2 or 2 steps to step 3. At step 2
        you can take 2 1 step to step 3 or 2 steps to step 4. 
        At step 3, you can take 1 step to step 4 but if you can't take 2 steps 
        because you're contrained by 4 total steps.


        Args:
            n (int): total number of steps you can take

        Returns:
            int: distinct ways of taking n steps given you can only take 1 or 2 steps at a time
        """
        if n == 1:
            return 1
        
        if n == 2:
            return 2
        
        
        prev1, prev2 = 1, 2
        for i in range (3, n+1):
            current = prev1 + prev2
            prev1 = prev2
            prev2 = current
            
        
        return prev2
    
    
 
solution = Solution()  
print(solution.climbStairs(10))
