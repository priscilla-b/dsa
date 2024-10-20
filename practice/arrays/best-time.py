# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        
        min_price = prices[0]
        max_profit = 0
    
        for price in prices[1:]:
            # for each day's price, calculate how much profit
            # you would make if you sold the stock on that day
            profit = price - min_price
            
            # update max profit if a higher profit is found
            max_profit = profit if profit > max_profit else max_profit
            
            # update min price if a lower price is found
            min_price = price if price < min_price else min_price
           
            
          
        return max_profit
    

   

solution = Solution()
print(solution.maxProfit2([7, 1, 5, 3, 6, 4]))
print(solution.maxProfit2([2, 4, 1]))
                
                