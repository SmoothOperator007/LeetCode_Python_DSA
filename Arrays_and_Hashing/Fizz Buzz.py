"""
Problem: [412. Fizz Buzz]
Difficulty: Easy

--- EXPECTED / OPTIMAL APPROACH ---
Pattern: Linear Scan / Arithmetic Simulation
Intuition: 
Iterate through numbers from 1 to n (1-indexed). For each number, check divisibility 
conditions in order of restrictiveness. Checking divisibility by both 3 and 5 first 
prevents shorter conditions from intercepting numbers that are multiples of both.

Time Complexity: O(n) - We visit each number from 1 to n exactly once.
Space Complexity: O(n) - Required to store the resulting string array of size n.

--- LEARNING ---
Custom Intuition & Logic:
- The range must be explicitly set from `1` to `n + 1` to account for Python's exclusive upper bound in `range()`.
- Placing the combined `i % 3 == 0 and i % 5 == 0` check at the top of the conditional block is crucial; otherwise, multiples of 15 would incorrectly trigger the single-condition `if i % 3 == 0` check first.
- The solution relies on basic modulus arithmetic, avoiding unnecessary data structures or complex pointer manipulation since a full linear traversal is required.
"""

class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        x = []
        for i in range(1, n + 1):
            if i % 3 == 0 and i % 5 == 0:
                x.append("FizzBuzz")
            elif i % 3 == 0:
                x.append("Fizz")
            elif i % 5 == 0:
                x.append("Buzz")
            else:
                x.append(str(i))
        return x
