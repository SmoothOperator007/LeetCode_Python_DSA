"""
Problem: [125. Valid Palindrome]
Difficulty: Easy

--- EXPECTED / OPTIMAL APPROACH ---
Pattern: Two Pointers (Opposite Direction)
Intuition: 
Use two pointers starting at opposite ends of the string and move them inward, 
skipping non-alphanumeric characters on the fly and comparing case-insensitively.

Time Complexity: O(n) - We traverse the string at most once.
Space Complexity: O(1) - No auxiliary memory or string copies are created.

--- LEARNING ---
- The two-pointer pattern avoids creating extra string copies in memory, achieving O(1) space efficiency.
- Your custom approach cleanly filtered characters using `isalnum()`, converted with `.lower()`, and checked equality via slicing (`x == x[::-1]`), successfully passing all test cases.
"""

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        x = ""
        for i in s:
            if i.isalnum():
                x += i
            else:
                continue
        x = x.lower()
        return x == x[::-1]


"""
--- OPTIMAL APPROACH CODE (Two Pointers) ---
"""

class SolutionOptimal(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        left, right = 0, len(s) - 1
        
        while left < right:
            # Skip non-alphanumeric characters from the left
            while left < right and not s[left].isalnum():
                left += 1
            # Skip non-alphanumeric characters from the right
            while left < right and not s[right].isalnum():
                right -= 1
                
            # Compare case-insensitively
            if s[left].lower() != s[right].lower():
                return False
                
            left += 1
            right -= 1
            
        return True
