# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/?envType=featured-list&envId=top-interview-questions?envType=featured-list&envId=top-interview-questions

# You are given an array 'price' where 'prices[i]' is the price of a given stock on the ith day.
# you want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.


from typing import List
# 1st solution
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        
        max_profit = 0
        min_price = prices[0]                         # initialize min_price as 1st index of prices
        
        for price in prices:
            min_price = min(min_price, price)         # compare current price and min_price
            cur_profit = price - min_price            
            max_profit = max(max_profit, cur_profit)
        
        return max_profit


# 2nd solution
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        max_profit = 0
        
        for cur_price in prices:
            if min_price > cur_price:
                min_price = cur_price
            profit = cur_price - min_price
            if profit > max_profit:
                max_profit = profit
        
        return max_profit

            
# Test
sol = Solution()
prices1 = [7,1,5,3,6,4]
print(sol.maxProfit(prices1))
prices2 = [7,6,4,3,1]
print(sol.maxProfit(prices2))









































