"""# Problem: Merge Sorted Array (LeetCode 88)
Difficulty: Easy
Pattern: Two Pointers (Backward Traversal)
Category: Arrays & Hashing / Sorting

--- EXPECTED / OPTIMAL APPROACH ---
- **Intuition:** Since both arrays are pre-sorted and `nums1` has trailing capacity (`0` placeholders) equal to the size of `nums2`, we can compare elements starting from the end of their valid portions (`m - 1` and `n - 1`) and place the larger element at the very end of `nums1` (`m + n - 1`). Working backwards avoids overwriting uncompared elements and eliminates extra space overhead.
- **Time Complexity:** $O(m + n)$ — Each element from `nums1` and `nums2` is visited at most once.
- **Space Complexity:** $O(1)$ — Modifies the array entirely in-place without auxiliary data structures.

--- STEP-BY-STEP PINTER LOGIC ---
1. `p1 = m - 1`: Points to the last valid element in `nums1`.
2. `p2 = n - 1`: Points to the last element in `nums2`.
3. `p = m + n - 1`: Points to the final index of `nums1` where the largest candidate goes.
4. **Comparison Loop:** While both pointers are within bounds, compare `nums1[p1]` and `nums2[p2]`. Assign the larger value to `nums1[p]`, decrement the corresponding source pointer and `p`.
5. **Clean-up Loop:** If any elements remain in `nums2` (i.e., `p1` ran out first), copy the remaining elements from `nums2` into `nums1`. (Remaining elements in `nums1` are already in place).
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
        p1 = m - 1
        p2 = n - 1
        p = m + n - 1
        
        while p1 >= 0 and p2 >= 0:
            if nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1
            p -= 1
            
        while p2 >= 0:
            nums1[p] = nums2[p2]
            p2 -= 1
            p -= 1
