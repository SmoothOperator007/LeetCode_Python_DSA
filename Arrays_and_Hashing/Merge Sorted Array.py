"""
Problem: Merge Sorted Array 
Difficulty: Easy

--- EXPECTED / OPTIMAL APPROACH ---
Pattern: Two Pointers (Backward Traversal)
- Intuition: Since both arrays are already sorted and `nums1` has built-in trailing space, 
  we can compare elements from the back (largest to smallest) using three pointers 
  (`p1` for end of `nums1`, `p2` for end of `nums2`, and `p` for the end of the merged space). 
  This avoids overwriting existing elements and eliminates the need for sorting.
- Time Complexity: O(m + n)
- Space Complexity: O(1)

--- LEARNING ---
- Custom Intuition: Instead of dealing with front-pointer shifts or complex zero checks, 
  we can target the exact tail of `nums1` using a reverse range (`range(-1, -n - 1, -1)`) 
  to drop `nums2` directly into the designated placeholder slots. 
- Trade-off: Applying Python's built-in `.sort()` after dumping elements results in 
  an O((m + n) log(m + n)) time complexity due to the sorting step, whereas the pure 
  two-pointer approach achieves O(m + n). However, the backward-index slot-fill pattern 
  provides a concise and practical alternative that executes efficiently within constraints.
- Complexity Trade-off: O((m + n) log(m + n)) time due to Timsort, with O(1) in-place space.
"""

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        index = 0
        for i in range(-1, -n - 1, -1):
            nums1[i] = nums2[index]
            index += 1
        return nums1.sort()
