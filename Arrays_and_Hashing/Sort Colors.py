"""
===============================================================================
Problem: Sort Colors (LeetCode #75)
Difficulty: Medium
Category: Two Pointers / Arrays & Hashing
===============================================================================

--- EXPECTED / OPTIMAL APPROACH ---
Pattern: Dutch National Flag Algorithm (3 Pointers, Single Pass)

Intuition:
- Use three pointers: `low` (boundary for 0s), `mid` (current element), and `high` (boundary for 2s).
- Traverse with `mid`:
  * If `nums[mid] == 0`: Swap with `nums[low]`, increment both `low` and `mid`.
  * If `nums[mid] == 1`: Increment `mid`.
  * If `nums[mid] == 2`: Swap with `nums[high]`, decrement `high` (do not advance `mid` yet, as swapped element needs checking).

Complexities:
- Time Complexity: O(N) — Single pass over the array.
- Space Complexity: O(1) — Mutates array in-place without extra memory allocation.


--- LEARNING & CUSTOM APPROACH ---
Intuition:
- Frequency counting approach (Two-Pass Bucket / Counting Sort).
- Pass 1: Count occurrences of 0, 1, and 2.
- Pass 2: Iterate through indices from 0 to len(nums)-1 and sequentially place values based on remaining count reserves.

Variable Logic & Control Flow:
- `count0`, `count1`, `count2` track remaining counts.
- `if count0 > 0:` -> overwrite with 0 and decrement `count0`.
- `elif count1 > 0:` -> overwrite with 1 and decrement `count1`.
- `else:` -> overwrite with 2 and decrement `count2`.

Trade-Offs & Complexity:
- Time Complexity: O(N) — Passes twice over array (1 pass to count, 1 pass to overwrite).
- Space Complexity: O(1) — Uses integer variables; zero auxiliary array memory.
- Performance: Achieved 0 ms (Beats 100.00%) runtime and 12.08 MB (Beats 95.62%) memory usage on LeetCode.

Key Takeaways:
1. In-place modification does not strictly require 1-pass swap algorithms if 2-pass counting maintains O(1) space.
2. Avoid constructing a new list (e.g., `[0]*count0 + ...`) because creating extra allocations violates O(1) auxiliary space constraints.
===============================================================================
"""

class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        count0 = 0
        count1 = 0
        count2 = 0

        # Pass 1: Count frequencies of 0, 1, and 2
        for i in nums:
            if i == 0:
                count0 += 1
            elif i == 1:
                count1 += 1
            elif i == 2:
                count2 += 1

        # Pass 2: Overwrite original array elements in-place using remaining counts
        for i in range(len(nums)):
            if count0 > 0:
                nums[i] = 0
                count0 -= 1
            elif count1 > 0:
                nums[i] = 1
                count1 -= 1
            else:
                nums[i] = 2
                count2 -= 1

        return nums
