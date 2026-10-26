"""
Problem: Group Anagrams (LeetCode 49)
Difficulty: Medium
Category: Arrays & Hashing / Strings & String Algorithms

--- EXPECTED / OPTIMAL APPROACH ---
Pattern: Hash Table with Canonical Key / Frequency Signature
Intuition: 
Anagrams share the exact same character makeup. To group them efficiently without 
repeatedly comparing every word against every other word ($O(M^2 \cdot N)$), we generate 
a unique, hashable signature for each word to use as a dictionary key:
1. Character frequency count mapped to a immutable tuple (or sorted string).
2. Store original strings inside lists grouped by their unique signature key.
Time Complexity: O(M * N) where M is the number of strings and N is the max string length.
Space Complexity: O(M * N) to store strings in the hash map.

--- LEARNING ---
My Custom Intuition & Logic:
- Built a dictionary (`dist = {}`) acting as a hash map bucket container.
- Iterated through every string `s` in `strs`.
- Handled dynamic bucket creation manually (`if key not in dist: dist[key] = []`) before appending the string.
- Extracted dictionary values and converted the view to a standard list using `list(dist.values())`.
- Trade-offs: Writing out manual existence checks avoids importing external modules like `collections.defaultdict`, giving full control over the underlying dictionary state while matching optimal performance.
"""

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        dist = {}
        for s in strs:
            # Generate sorted string signature as canonical key
            key = "".join(sorted(s))
            
            # Manual bucket initialization
            if key not in dist:
                dist[key] = []
                
            dist[key].append(s)
            
        return list(dist.values())
