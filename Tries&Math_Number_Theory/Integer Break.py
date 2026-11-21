"""
Problem: 343. Integer Break
Difficulty: Medium
Link: https://leetcode.com/problems/integer-break/

--- EXPECTED / OPTIMAL APPROACH ---
Pattern: Math / Number Theory (Greedy Factor Decomposition around e)
Intuition:
  To maximize the product of positive integers summing to n (with at least two
  parts), splitting into equal parts of size x gives x^(n/x), whose continuous
  maximum occurs at x = e ≈ 2.718. Among integers, 3 is closest to e and gives
  a higher product for equal sums than 2 (3 * 3 = 9 > 2 * 2 * 2 = 8).
  - For n = 2 and n = 3, the problem requires at least two integers, forcing
    1 + 1 = 2 (product 1) and 1 + 2 = 3 (product 2).
  - For n >= 4, divide n by 3 using quotient and remainder:
      * remainder == 0: product is 3^quotient.
      * remainder == 1: avoid multiplying by a leftover 1; combine one 3 and
        the remainder 1 into 2 + 2 = 4 -> 3^(quotient - 1) * 4.
      * remainder == 2: product is (3^quotient) * 2.

Time Complexity: O(1) (exponentiation of built-in integers scales with bit length,
  treated as O(1) under standard interview constraints).
Space Complexity: O(1).

--- LEARNING ---
Custom Intuition & Variable Logic:
  - Explicit early returns for n == 2 (returns 1) and n == 3 (returns 2) isolate
    the small cases where splitting reduces or caps the product due to the k >= 2
    constraint.
  - `quotient, remainder = divmod(n, 3)` computes both the count of 3s and the
    leftover in a single step:
      * `remainder == 0`: `3 ** quotient` uses all `quotient` threes cleanly.
      * `remainder == 1`: `(3 ** (quotient - 1)) * 4` borrows one `3` from the
        `quotient` threes and pairs it with the `1` remainder to form `4`
        (2 + 2), which beats 3 * 1 = 3.
      * `remainder == 2`: `(3 ** quotient) * 2` keeps all `quotient` threes and
        multiplies by the remaining `2`.

Complexity Trade-offs vs. Optimal Way:
  - Matches the optimal O(1) time and O(1) space complexity directly.
  - Compared to an O(n^2) or O(n) dynamic programming approach, this avoids
    allocating a DP array and computing subproblem transitions, running in 0 ms
    and 11.96 MB on LeetCode.
"""


class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 2:
            return 1
        if n == 3:
            return 2

        quotient, remainder = divmod(n, 3)

        if remainder == 0:
            return 3 ** quotient
        elif remainder == 1:
            return (3 ** (quotient - 1)) * 4
        else:  # remainder == 2
            return (3 ** quotient) * 2
