"""
Problem: 3105. Longest Strictly Increasing or Strictly Decreasing Subarray
Difficulty: Easy

--- EXPECTED / OPTIMAL APPROACH ---
Pattern: Linear Scan / Sliding Window
Intuition: 
To find the longest monotonic subarray, we can iterate through the array and track the lengths of contiguous strictly increasing and strictly decreasing segments. Whenever the rule is broken (or elements are equal), the respective sequence length resets to 1, while a global maximum variable (`max_len`) records the peak length encountered across both trends.
Time Complexity: O(N) since we traverse the array of length N once.
Space Complexity: O(1) as only a few scalar variables are maintained.

--- LEARNING ---
- Custom Intuition: Comparing adjacent elements using `range(len(nums) - 1)` (`nums[i]` and `nums[i+1]`) keeps index access intuitive and clean without risking out-of-bounds exceptions.
- Variable Logic: Starting `inc` and `dec` counters at `1` is crucial because any single element is inherently a valid monotonic subarray of length 1. 
- Reset Behavior: When a trend reverses or elements are equal, resetting the broken trend's counter back to `1` ensures it immediately starts fresh from the current boundary.
"""

class Solution(object):
    def longestMonotonicSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
            
        inc = 1
        dec = 1
        max_len = 1
        
        for i in range(len(nums) - 1):
            if nums[i] < nums[i + 1]:
                inc += 1
                dec = 1
            elif nums[i] > nums[i + 1]:
                dec += 1
                inc = 1
            else:
                inc = 1
                dec = 1
                
            max_len = max(max_len, inc, dec)
            
        return max_len
