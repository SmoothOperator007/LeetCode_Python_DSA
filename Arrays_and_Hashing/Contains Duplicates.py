"""
Problem: 217. Contains Duplicate
Difficulty: Easy

--- EXPECTED / OPTIMAL APPROACH ---
Pattern: Hash Set / Frequency Tracking
Intuition: 
To determine if any value appears at least twice in an array efficiently, we use a hash set to keep track of elements we have already encountered. 
A set uses a hash table internally: when we check `num in seen` or `seen.add(num)`, Python calculates a hash for the element to locate or 
store it in O(1) average time, completely avoiding sequential scans.

Complexity:
- Time Complexity: O(N) on average, since we traverse the array of length N at most once, and hash set lookups/insertions operate in O(1) average time.
- Space Complexity: O(N) to store the elements in the set in the worst-case scenario (all distinct elements).

--- LEARNING ---
Mistakes Made & Iterative Journey:
1. Initial TLE (Time Limit Exceeded) with Lists: 
   - Tried checking duplicates using a list `seen = []` with `num in seen`. 
   - Issue: List membership checking requires a sequential scan from the beginning, taking O(N) time in the worst case. 
     Doing this inside an iteration over N elements results in total operations proportional to 0 + 1 + 2 + ... + (N-1) = N(N-1)/2, 
     yielding an O(N^2) time complexity. For 100,000 elements, this triggers a TLE (~5 billion operations).
2. Wrong Answer via Direct Set-to-List Comparison: 
   - Tried comparing the set directly to the list (`if x == nums:`). 
   - Issue: A Python `set` and a `list` are distinct types and will never evaluate to equal (`set == list` is always False). 
     Furthermore, list equality checks exact element ordering.
3. Length-Based Set Comparison Approach:
   - Tried comparing lengths: `if len(set(nums)) == len(nums): return False else: return True`.
   - Issue: While this is correct and concise, it constructs a set from the entire array before checking lengths,
     meaning it doesn't allow early exit upon finding the first duplicate.
4. Key Takeaways on Data Structures:
   - List: Use when you need an ordered collection and searching every element sequentially is acceptable.
   - Set: Use when you need to efficiently check whether an element exists in O(1) average time via hash tables.
   - Dictionary: Use when you need to associate keys with values or count frequencies.
   - Interview Best Practice: Iterating with an explicit hash set and returning immediately upon finding a duplicate is preferred because 
     it allows early exit and avoids processing the entire array when a duplicate appears early.
"""

class Solution(object):
    def containsDuplicate(self, nums):
        """:type nums: List[int]
        :rtype: bool"""
        # Approach 1: Length-based set comparison
        if len(set(nums)) == len(nums):
            return False
        else:
            return True
            
        # Approach 2: Optimal hash set traversal (Early Exit)
        # seen = set()
        # for num in nums:
        #     if num in seen:
        #         return True
        #     seen.add(num)
        # return False
