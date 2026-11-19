class Solution:
    def maxProfit_bf(self, prices: list[int]) -> int:
        """
        Brute force solution: O(n^2) time complexity, O(1) space complexity
        Since we have to buy before we sell, we iterate throught the list first 
        to find the buy price, and then iterate through the rest of the list to find
        the sell price that maximizes the profit. 
        Args:
            prices (list[int]): list of prices of a stock on different days
        Returns:
            int: maximum profit that can be made from buying and selling the stock
        """
        max_profit = 0
        for i in range(len(prices)):
            for j in range(i+1, len(prices)):
                current_profit = prices[j] - prices[i]
                max_profit = current_profit if current_profit > max_profit else max_profit
           
        return max_profit
    
    def maxProfit(self, prices: list[int]) -> int:
        max_profit = 0
        sell_prices = {i : prices[i] for i in range(1, len(prices))}
        print(sell_prices)
        for i in range(len(prices)-1):
            current_profit = sell_prices[i+1] - prices[i]
            max_profit = current_profit if current_profit > max_profit else max_profit

        return max_profit

solution = Solution()
print(solution.maxProfit([7,1,5,3,6,4])) #