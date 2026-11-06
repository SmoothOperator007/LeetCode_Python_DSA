"""
Problem: Majority Element
Difficulty: Easy

--- EXPECTED / OPTIMAL APPROACH ---
1. Boyer-Moore Majority Vote Algorithm:
   - Intuition: Since the majority element appears more than ⌊n / 2⌋ times, it will always outvote other elements. We maintain a candidate and a counter. If the counter drops to 0, we pick the current number as the new candidate.
   - Time Complexity: O(n) because we iterate through the list once.
   - Space Complexity: O(1) as we only use two variables (`candidate` and `count`).

2. Hash Map Frequency Counting:
   - Intuition: Count the frequency of each element using a hash map and return the element with the maximum frequency.
   - Time Complexity: O(n) to build the frequency map and find the maximum key.
   - Space Complexity: O(n) to store the counts of unique elements in the dictionary.

--- LEARNING ---
- Custom Implementation: Your approach explicitly separates the check for distinct elements (`if i not in counts`) to initialize frequencies and increments existing keys. This is very clear and maps directly to fundamental dictionary operations.
- Trade-offs: While the hash map approach uses O(n) extra space, it is extremely versatile for various frequency-based problems (like Top K Frequent Elements or Most Frequent Even Element) where Boyer-Moore's voting logic cannot be directly applied.
"""

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        counts = {}
        
        for i in nums:
            if i not in counts:
                counts[i] = 1
            else:
                counts[i] += 1
                
        return max(counts, key=counts.get)
