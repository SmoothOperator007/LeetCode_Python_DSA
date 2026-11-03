"""
Problem: Minimum Moves to Equal Array Elements III
Difficulty: Easy / Medium (Variant)

--- EXPECTED / OPTIMAL APPROACH ---
Pattern: Math & Greedy Reduction / Array Iteration
Intuition:
To make all elements equal by incrementing individual elements, every number must 
ultimately reach the maximum value present in the array. 

Complexity:
- Time Complexity: O(N) to find the maximum value and iterate through the array.
- Space Complexity: O(1) auxiliary space.

--- LEARNING ---
- Explicit Iteration: Using a running accumulator (`moves += melm - i`) provides an intuitive, highly readable breakdown of the distance calculation for each element.
- Complexity Balance: Achieves identical O(N) time efficiency to more concise built-in functions while keeping variable updates explicit and easy to debug.
"""

class Solution(object):
    def minMoves(self, nums):
        """:type nums: List[int]
        :rtype: int
        """
        melm = max(nums)
        moves = 0
        for i in nums:
            moves += melm - i
        return moves
