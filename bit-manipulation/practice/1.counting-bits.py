# https://leetcode.com/problems/counting-bits/

class Solution:
    
    def count_bits_n(self, n: int) -> list[int]:
        """
        Brute force approach. iterate through range of (n+1) values
        and then for each value try converting to binary in order to 
        count how many 1s are in each
        """
        
        count_array = []
        for i in range(n+1):
            count_array.append(self.count_one_bit_n(i))
            
        return count_array
    
    
    def count_one_bit_n(self, i:int) -> int:
        one_count = 0
        if i == 0:
            return one_count
        
        while i > 0:
            one_count += i % 2
            i //= 2        
            
        return one_count
    
    
    def count_bits(self, n:int) -> list[int]:
        """
        Using Kernighan's Algorithm: 

        
        """
        
        count_array = []
        for i in range(n+1):
            count_array.append(self.count_one_bit(i))
            
        return count_array
    
    def count_one_bit(self, i:int) -> int:
        one_count = 0
        while i > 0:
            i &= (i - 1)  # Remove the lowest set bit
            one_count += 1
        return one_count
        
    
    
    
solution = Solution()
print(solution.count_bits(5))
        
        
       