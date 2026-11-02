"""
Problem: Maximum Ice Cream Bars (LeetCode 1833)
Difficulty: Medium

--- EXPECTED / OPTIMAL APPROACH ---
Pattern: Greedy Choice + Sorting
Intuition: 
To maximize the number of ice cream bars you can buy with a fixed amount of coins, 
you should always prioritize buying the cheapest bars first. Sorting the cost array 
in ascending order allows us to iterate from the lowest cost to the highest, 
greedily purchasing items until our coin balance is insufficient.

Complexity:
- Time Complexity: O(n log n) due to the sorting step, where n is the number of ice cream bars.
- Space Complexity: O(1) or O(n) depending on the sorting implementation used in Python (Timsort).

--- LEARNING ---
Custom Intuition & Execution:
- Your solution correctly uses the greedy property: sorting elements ensures we never waste coins on expensive items when cheaper ones are available.
- Using a strict `if coins >= i` check followed by decrementing coins and incrementing the count, with an early exit (`else: return count`), ensures optimal runtime performance on valid test cases.
- Trade-off: While $O(n \log n)$ sorting is extremely clean and efficient for general constraints, a Counting Sort approach could theoretically achieve $O(n + k)$ if the maximum cost $k$ is small, though sorting remains the preferred interview standard for readability and maintainability.
"""

class Solution(object):
    def maxIceCream(self, costs, coins):
        """
        :type costs: List[int]
        :type coins: int
        :rtype: int
        """
        costs.sort()
        count = 0
        for i in costs:
            if coins >= i:  #or i <= coins
                count += 1
                coins -= i
            else:
                return count
        return count
