"""
===============================================================================
Problem: 121. Best Time to Buy and Sell Stock
Difficulty: Easy
Category / Pattern: Arrays & Hashing / Greedy
===============================================================================

--- EXPECTED / OPTIMAL APPROACH ---
Intuition:
  To maximize profit from a single buy and sell transaction, we need to find 
  the lowest buying price and the highest selling price that occurs *after* that buy date. 
  By iterating through the array once, we track the minimum price seen so far and 
  evaluate the potential profit at each step.

Time Complexity: O(N)
  - Single traversal of the price array of length N.
Space Complexity: O(1)
  - Uses only scalar tracking variables (`min_price` and `max_profit`).

--- LEARNING ---
Your Custom Intuition & Logic:
  - Initialized `min_price` to `prices[0]` to set the initial baseline using the first element.
  - Used an `if-elif` control flow:
      1. If the current price is lower than the recorded minimum, update `min_price`.
      2. Otherwise, check if selling at the current price yields a new maximum profit.
  - This avoids redundant checks or nested loops, keeping execution clean and efficient.

Trade-offs & Notes:
  - Assumes a non-empty `prices` list where `prices[0]` is safely accessible.
===============================================================================
"""

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        min_price = prices[0]
        max_profit = 0
        
        for price in prices:
            if price < min_price:
                min_price = price
            elif price - min_price > max_profit:
                max_profit = price - min_price
                
        return max_profit
