
# https://leetcode.com/problems/climbing-stairs

class Solution:
    def climbStairs(self, n: int) -> int:
        """At any point in time, you can only take 1 or 2 steps at a time.
        So say you're currently at step0 on your staircase you only need to take 1 step to
        get to step1. At step1, you can take 1 step to get to step2 or 2 steps to get to step3.
        At step2, you can take 1 step to get to step3 or 2 steps to get to step4, and so on.
        You could have also taken 2 steps to get to step2 from step0, and then from there taken 1 step
        to get to step3 or 2 steps to get to step4.
        From this, there are three ways to get to step3: 2 ways if you'd taken 1 step from step0 or 
        1 way if you'd taken 2 steps from step0.


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
