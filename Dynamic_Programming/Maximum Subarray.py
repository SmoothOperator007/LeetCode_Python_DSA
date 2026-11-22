"""
Problem: 53. Maximum Subarray
Difficulty: Medium
Link: https://leetcode.com/problems/maximum-subarray/?envType=problem-list-v2&envId=array

--- EXPECTED / OPTIMAL APPROACH ---
Pattern: Dynamic Programming (Kadane's Algorithm)

Intuition:
Any contiguous subarray ending at index i either starts fresh at nums[i] or
extends the best contiguous subarray ending at index i - 1. If the running sum
before nums[i] is negative (or adds less than starting fresh), starting at
nums[i] is strictly better. Keeping a global maximum captures the highest sum
seen across all ending positions.

Time Complexity: O(n), where n is the length of nums (single pass).
Space Complexity: O(1), using only constant state variables.

--- LEARNING ---
Custom Intuition & Variable Logic:
- Initializing both `current_sum` and `max_sum` to `nums[0]` establishes a
  valid baseline for non-empty arrays without assuming `0` is a valid subarray
  sum. This is critical when all numbers in `nums` are negative (for example,
  `[-3, -1, -2]` should return `-1`, not `0`).
- Iterating through `nums[1:]` avoids re-evaluating index 0 while checking every
  subsequent element.
- `current_sum = max(num, current_sum + num)` represents the best contiguous
  subarray sum ending at `num`: either `num` starts a new subarray, or it
  appends to `current_sum`.
- `max_sum = max(max_sum, current_sum)` updates the answer whenever the
  subarray ending at `num` beats the best sum found earlier.

Complexity & Trade-offs vs. Optimal Way:
- This implementation matches the optimal O(n) time and O(1) space complexity
  expected in interviews.
- Trade-off: `nums[1:]` creates a slice view/copy in Python (O(n) memory
  overhead for the slice iterator in theory, though negligible in practice);
  using `range(1, len(nums))` or `iter(nums)` with `next()` avoids
  creating a slice object at all.
- Also note: this tracks the maximum sum only, not the start and end indices
  of the subarray; tracking start/end pointers is a straightforward extension
  if indices are ever requested.
"""


class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        current_sum = nums[0]
        max_sum = nums[0]

        for num in nums[1:]:
            current_sum = max(num, current_sum + num)
            max_sum = max(max_sum, current_sum)

        return max_sum
