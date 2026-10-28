"""
Problem: Length of Last Word (LeetCode)
Difficulty: Easy

--- EXPECTED / OPTIMAL APPROACH ---
Pattern: String Manipulation & Built-in Slicing
Intuition: 
Instead of tracking characters manually, the expected optimal approach leverages 
Python's built-in `.split()` method. It automatically strips surrounding whitespace and keeps the spaces in between the words (THIS IS INBUILT)
and splits the string by spaces into a list of words, giving instant access to the last element.

Time Complexity: O(n) where n is the length of the string, as splitting scans characters once.
Space Complexity: O(n) to store the resulting list of words in memory.

--- LEARNING ---
My Custom Approach:
1. Stripped surrounding whitespace from the string using `.strip()`.
2. Iterated character-by-character through the string with a `current_word` string accumulator.
3. Appended `current_word` to a `words` list upon hitting spaces and reset the accumulator.
4. Added an explicit check after the loop to capture the final word since strings might not end with a space.
5. Returned the length of the last item via `len(words[-1])`.

Trade-offs: 
Writing a manual character parser is a great exercise for low-level string traversal and handling edge cases, but the built-in one-liner is more concise 
and optimized in C under the hood.
"""

class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        # --- OPTIMAL ONE-LINER APPROACH ---
        return len(s.split()[-1])
        
        # --- MY CUSTOM ITERATIVE APPROACH ---
        s = s.strip()
        words = []
        current_word = ""
        
        for i in s:
            if i == ' ':
                if current_word != "":
                    words.append(current_word)
                    current_word = ""
            else:
                current_word += i
                
        if current_word != "":
            words.append(current_word)
            
        return len(words[-1])
