"""
Problem: 34. Find First and Last Position of Element in Sorted Array
Difficulty: Medium
Link: https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/description/

--- EXPECTED / OPTIMAL APPROACH ---
Pattern: Binary Search (Boundary Search)
Intuition:
Since the array is sorted in non-decreasing order and the problem requires O(log n) time complexity, a standard linear scan or array mutation approach is insufficient. Instead, we can run two modified binary searches:
1. findFirst: When nums[mid] == target, we record the index and continue searching in the left half (right = mid - 1) to find the absolute first occurrence.
2. findLast: When nums[mid] == target, we record the index and continue searching in the right half (left = mid + 1) to find the absolute last occurrence.

Complexity:
- Time Complexity: O(log n), because each helper function halves the search space iteratively.
- Space Complexity: O(1), as only a few pointers and index variables are maintained.

--- LEARNING ---
- Why linear approaches fail: Using loops with `nums.index()` or modifying list elements linearly operates in O(n) time, failing interview constraints and requirement specifications.
- Pointer & Variable Logic: Using separate helper functions with `left` and `right` boundaries prevents pointer overlap confusion and cleanly captures boundary indices using an `idx = -1` sentinel default.
"""

class Solution(object):
    def searchRange(self, nums, target):
        def findFirst(nums, target):
            left, right = 0, len(nums) - 1
            idx = -1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] >= target:
                    right = mid - 1
                else:
                    left = mid + 1
                if nums[mid] == target:
                    idx = mid
            return idx

        def findLast(nums, target):
            left, right = 0, len(nums) - 1
            idx = -1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] <= target:
                    left = mid + 1
                else:
                    right = mid - 1
                if nums[mid] == target:
                    idx = mid
            return idx

        return [findFirst(nums, target), findLast(nums, target)]
