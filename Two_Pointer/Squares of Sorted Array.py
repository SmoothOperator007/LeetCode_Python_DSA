"""
Problem: Squares of a Sorted Array (LeetCode)
Difficulty: Easy

--- ORIGINAL ACCEPTED APPROACH ---
Pattern: In-place Square & Sort
Intuition: 
Iterate through the array to square each element in-place, then call Python's built-in .sort() method to arrange the squared numbers in non-decreasing order.
Time Complexity: O(n log n) - Dominated by the sorting step.
Space Complexity: O(1) or O(n) depending on Python's internal sorting implementation (Timsort).

--- EXPECTED / OPTIMAL APPROACH ---
Pattern: Two Pointers
Intuition: 
Since the input array is already sorted, the largest squared values will always be at the extreme ends (left or right) because squaring negative numbers makes them positive. We can initialize two pointers at both ends and fill a result array from right to left by picking the larger absolute value.
Time Complexity: O(n) - We traverse the array a single time.
Space Complexity: O(n) - Required to store the output result array.
"""

class Solution(object):
    def sortedSquares(self, nums):
        """:type nums: List[int]"""
        """:rtype: List[int]"""
        
        # --- 1. Your Original Accepted Code (In-place & Sort) ---
        for i in range(len(nums)):
            nums[i] = nums[i] ** 2
        nums.sort()
        return nums


class OptimalSolution(object):
    def sortedSquares(self, nums):
        """:type nums: List[int]"""
        """:rtype: List[int]"""
        
        # --- 2. Optimal O(n) Two-Pointer Approach ---
        n = len(nums)
        res = [0] * n
        left, right = 0, n - 1
        
        for i in range(n - 1, -1, -1):
            if abs(nums[left]) > abs(nums[right]):
                res[i] = nums[left] ** 2
                left += 1
            else:
                res[i] = nums[right] ** 2
                right -= 1
                
        return res
