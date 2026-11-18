"""
Problem: Find the Difference (LeetCode 389)
Difficulty: Easy

--- EXPECTED / OPTIMAL APPROACH ---
Pattern: Bit Manipulation (XOR) / ASCII Sum
- Intuition: Since string `t` contains all characters of `s` plus one extra character, 
  XORing every character's ASCII value from both strings together will cancel out 
  all identical pairs. The remaining value is the extra character.
- Time Complexity: O(n) where n is the length of string t.
- Space Complexity: O(1) auxiliary space.

--- LEARNING ---
- Custom Iteration & Sorting: We analyzed why strings are immutable in Python and 
  how sorting both strings allows a linear scan to instantly pinpoint mismatches. 
- Trade-offs: While sorting takes O(n log n) time, it provides an intuitive step-by-step 
  verification flow compared to bitwise operators.
"""

class Solution(object):
    def findTheDifference(self, s, t):
        # Approach 1: Sorting & Linear Scan
        s_sorted = sorted(s)
        t_sorted = sorted(t)
        
        for i in range(len(s)):
            if s_sorted[i] != t_sorted[i]:
                return t_sorted[i]
                
        return t_sorted[-1]

    def findTheDifference_xor(self, s, t):
        # Approach 2: Optimal XOR Bitwise Solution
        result = 0
        for char in s + t:
            result ^= ord(char)
        return chr(result)
