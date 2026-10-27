"""
LeetCode Problem 342: Power of Four
Difficulty: Easy

--- EXPECTED / OPTIMAL APPROACH ---
Pattern: Bit Manipulation & Math (O(1) Time, O(1) Space)
- Intuition: A number n is a power of four if:
  1. n > 0 (positive integer)
  2. (n & (n - 1)) == 0 (it is a power of two, ensuring only one bit is set)
  3. (n & 0x55555555) != 0 (the single set bit is located at an even-indexed position, 
     since powers of 4 like 4^0=1, 4^1=4, 4^2=16 have bits at positions 0, 2, 4...)
- Time Complexity: O(1) - Evaluated using constant bitwise operations.
- Space Complexity: O(1) - No extra memory allocated.

--- LEARNING ---
- Custom Intuition: Your iterative approach divides n by 4 in a while loop, 
  running in O(log_4 n) time and O(1) space. It correctly validates non-multiples 
  and handles zero/negative bounds gracefully.
- Trade-off: While trial division is intuitive and easy to write under interview pressure, 
  optimizing it to bit manipulation fulfills the follow-up constraint of solving it 
  without loops or recursion.
"""

class Solution(object):
    def isPowerOfFour(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 1:
            return True
        elif n == 0:
            return False
        
        if n > 0:
            while n != 1:
                if n % 4 == 0:
                    n = n / 4
                else:
                    return False
            return True
        elif n < 0:
            return False

#this is the expected approach 

class Solution(object):
    def isPowerOfFour(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # Optimal Bit Manipulation Approach (O(1) Time, O(1) Space)
        return n > 0 and (n & (n - 1)) == 0 and (n & 0x55555555) != 0

    def isPowerOfFourRecursive(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # Recursive Approach (O(log_4 n) Time, O(log_4 n) Space)
        if n == 1:
            return True
        if n <= 0 or n % 4 != 0:
            return False
        return self.isPowerOfFourRecursive(n // 4)
