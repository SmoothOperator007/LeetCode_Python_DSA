"""
Problem: Ugly Number (LeetCode 263)
Difficulty: Easy

--- EXPECTED / OPTIMAL APPROACH ---
Pattern: Number Theory & Prime Factorization
Intuition: 
An ugly number is a positive integer whose prime factors are limited to 2, 3, and 5. 
By iteratively dividing the number by 2, 3, and 5 as long as it remains divisible, any valid 
ugly number will eventually reduce down to 1. If any other prime factor remains, the number 
will get stuck before reaching 1 and fail.
Time Complexity: O(log n) because the number is repeatedly divided by 2, 3, or 5.
Space Complexity: O(1) as it uses constant extra space.

--- LEARNING ---
Custom Intuition & Logic:
- Handled non-positive numbers (`n <= 0`) and the base case `n == 1` immediately to prevent infinite loops and ensure correctness.
- Used sequential checks for factors 2, 3, and 5 inside a `while n > 1` loop, returning `False` immediately if an unexpected divisor is encountered in the `else` block.
Trade-offs:
- While slightly more verbose than a compact `for p in [2, 3, 5]:` loop, the explicit `if/elif/else` chain provides crystal-clear readability and achieves optimal 0 ms runtime (100% beats on LeetCode).
"""

class Solution(object):
    def isUgly(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n < 0 or n == 0:
            return False
        elif n == 1:
            return True
            
        while n > 1:
            if n % 2 == 0:
                n = n / 2
            elif n % 3 == 0:
                n = n / 3
            elif n % 5 == 0:
                n = n / 5
            else:
                return False
                
        return n == 1
