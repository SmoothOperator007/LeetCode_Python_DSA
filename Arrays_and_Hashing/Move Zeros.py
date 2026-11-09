"""
LeetCode 283 - Move Zeroes
Difficulty: Easy

--- EXPECTED / OPTIMAL APPROACH ---
Pattern: Two Pointers (Same-Direction)
Intuition: 
Maintain a pointer (last_non_zero_found_at) to keep track of the insertion position for non-zero elements.
Iterate through the array with a second pointer; whenever a non-zero element is encountered, swap it with 
the element at the insertion pointer and increment the insertion pointer. This pushes all zeros to the 
end while maintaining the relative order of non-zero elements.

Complexity:
- Time Complexity: O(n), where n is the number of elements in the array. We iterate through the array once.
- Space Complexity: O(1), as the operation is performed strictly in-place.

--- LEARNING ---
Your Custom Intuition & Logic:
- You successfully applied the classic same-direction two-pointer technique to solve the problem in-place without 
  allocating extra space.
- The swap mechanism `nums[last_non_zero_found_at], nums[i] = nums[i], nums[last_non_zero_found_at]` ensures that 
  non-zero elements are cleanly shifted forward while preserving their relative order.
- Complexity Trade-offs: Your solution achieves optimal performance with linear time and constant extra space.
"""

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        last_non_zero_found_at = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[last_non_zero_found_at], nums[i] = nums[i], nums[last_non_zero_found_at]
                last_non_zero_found_at += 1
