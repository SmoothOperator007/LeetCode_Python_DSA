"""
Problem: Valid Anagram
Difficulty: Easy
Platform: LeetCode

--- EXPECTED / OPTIMAL APPROACH ---
Pattern: Hash Map Frequency Counting / Single-Map Consumption
Intuition: 
An anagram requires both strings to have identical character counts. While building two 
separate frequency dictionaries and comparing them works conceptually and intuitively, 
optimizing the approach involves building one map and decrementing it with the second 
string to save memory and dictionary-comparison overhead.

Time Complexity: O(N) where N is the length of the strings.
Space Complexity: O(K) where K is the number of unique characters in the strings.

--- LEARNING ---
- Length validation acts as an efficient O(1) guard clause to eliminate mismatched strings early.
- Explicit if-else blocks for dictionary initialization (`if i not in counters: counters[i] = 1 else: ...`) 
  make the frequency counting logic transparent and easy to trace.
- Direct dictionary comparison (`counters == countert`) cleanly leverages Python's built-in 
  equality operators for key-value pair checks.
"""

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False 
        
        counters = {}
        countert = {}

        for i in s:
            if i not in counters:
                counters[i] = 1
            else:
                counters[i] = counters[i] + 1
        
        for i in t:
            if i not in countert:
                countert[i] = 1
            else:
                countert[i] = countert[i] + 1

        if counters == countert:
            return True
        else:
            return False
