"""
Problem: Number of Segments in a String (LeetCode 434)
Difficulty: Easy

--- EXPECTED / OPTIMAL APPROACH ---
Pattern: String Parsing / Character Scanning
Intuition: 
A segment in a string is defined as a contiguous sequence of non-space characters. 
We can solve this efficiently using Python's built-in `split()` method to parse 
and count tokens, or by scanning indices directly to optimize auxiliary space.

Time Complexity: O(n) where n is the length of the string.
Space Complexity: O(n) for the split list approach, or O(1) for the in-place counter approach.

--- LEARNING ---
- Built-In Approach: `len(s.split())` leverages internal C-optimized string parsing, instantly handling leading, trailing, and multiple spaces in a single concise line.
- Custom In-Place Approach: Checking boundary conditions (`s[i] != ' ' and (i == 0 or s[i - 1] == ' ')`) avoids extra memory overhead by tracking segment starts on the fly.
"""

class Solution(object):
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Approach 1: The concise one-liner using split()
        # return len(s.split())
        
        # Approach 2: Custom in-place character traversal (Beats 100%)
        count = 0
        for i in range(len(s)):
            # A segment starts if the current character is not a space,
            # and it's either the first character or preceded by a space
            if s[i] != ' ' and (i == 0 or s[i - 1] == ' '):
                count += 1
        return count
