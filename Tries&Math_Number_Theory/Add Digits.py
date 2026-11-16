"""
Problem: 258. Add Digits
Difficulty: Easy

--- EXPECTED / OPTIMAL APPROACH ---
Pattern: Mathematical Digital Root
Intuition: 
Repeatedly summing the digits of a number until a single digit remains corresponds 
to the digital root of the number. For any positive integer, this can be calculated 
directly in constant time using modular arithmetic: 1 + (num - 1) % 9 (with num = 0 
returning 0).
Complexity:
- Time Complexity: O(1)
- Space Complexity: O(1)

--- LEARNING ---
My Approach:
- Used an iterative extraction loop coupled with Python lists to isolate each digit 
  via modulo (`num % 10`) and floor division (`num //= 10`).
- Collected digits into a local `digits` list on each pass and aggregated them using `sum()`.
- Repeated the outer loop while `num >= 10` until the value reduced to a single digit.
Complexity Trade-offs:
- Time Complexity: O(log_{10}(N)) because the number of digits decreases logarithmically 
  with each outer iteration.
- Space Complexity: O(log_{10}(N)) to store the digits of the number in the list during 
  each extraction phase.
"""

class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        while num >= 10:
            digits = []
            
            # Extract each digit and append to the list
            while num > 0:
                digits.append(num % 10)
                num //= 10
                
            # Sum up all the digits in the list for the next iteration
            num = sum(digits)
            
        return num


#this now is uisng formuala

        return 0 if num == 0 else 1 + (num - 1) % 9
