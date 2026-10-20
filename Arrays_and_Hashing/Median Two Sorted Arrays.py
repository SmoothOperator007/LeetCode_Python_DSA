"""
Problem: Median of Two Sorted Arrays (LeetCode 4)
Difficulty: Hard

--- EXPECTED / OPTIMAL APPROACH ---
Pattern: Binary Search on Partition
Intuition: 
To satisfy the strict O(log (m + n)) time complexity required by the problem description, 
we perform a binary search on the smaller array to find a valid partition index `i` in nums1 
and `j` in nums2 such that the combined left half contains elements all smaller than or 
equal to the elements in the combined right half.
Time Complexity: O(log(min(m, n)))
Space Complexity: O(1)

--- LEARNING ---
My Custom Approaches:
1. Concatenation & Sort: 
   - Intuition: Combine both lists into a single array, sort it, and find the middle index.
   - Trade-off: Very simple to write and understand, but takes O((m + n) log(m + n)) time due to sorting, 
     though it performs extremely well in practice for small constraints.
2. Two-Pointer Walk:
   - Intuition: Since both arrays are already individually sorted, we can use two pointers (i and j) 
     to step through both arrays simultaneously up to the middle index, tracking `curr` and `prev` values.
   - Trade-off: Runs in O(m + n) time and O(1) space, avoiding the heavy overhead of global sorting 
     while remaining much easier to reason about than the binary search partition.
"""

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        # --- Approach 1: Concatenation and Sort (Your First Accepted Solution) ---
        nums3 = nums1 + nums2
        nums3.sort()
        total_len = len(nums3)
        
        if total_len % 2 != 0:
            return float(nums3[total_len // 2])
        else:
            return (nums3[total_len // 2] + nums3[(total_len // 2) - 1]) / 2.0


        """
        for i in range(len(nums2)):
            nums1.append(nums2[i])
        nums1.sort()

        if len(nums1)%2 != 0:
            return nums1[(len(nums1)//2)]
        else:
            return ((nums1[(len(nums1)/2)])+(nums1[(len(nums1)/2)-1]))/2.0
        """

        #This is another way i tried to optimize the time space complexities

        # --- Approach 2: Two-Pointer Walk (Your Conceptual Approach) ---
        # m, n = len(nums1), len(nums2)
        # total_len = m + n
        # mid = total_len // 2
        # i, j = 0, 0
        # curr, prev = 0, 0
        # 
        # for _ in range(mid + 1):
        #     prev = curr
        #     if i < m and (j >= n or nums1[i] <= nums2[j]):
        #         curr = nums1[i]
        #         i += 1
        #     else:
        #         curr = nums2[j]
        #         j += 1
        #         
        # if total_len % 2 != 0:
        #     return float(curr)
        # else:
        #     return (prev + curr) / 2.0
