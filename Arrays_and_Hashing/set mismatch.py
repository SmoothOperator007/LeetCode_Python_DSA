"""
Problem: 645. Set Mismatch
Difficulty: Easy

--- EXPECTED / OPTIMAL APPROACH ---
Optimal Pattern: In-Place Index Marking (or Math / Hash Set)
Intuition:
- Since nums has length n and values are meant to be 1..n, each value v
  maps to index abs(v) - 1.
- Walk through nums: mark visited numbers by negating nums[abs(num) - 1].
  If nums[abs(num) - 1] is already negative, abs(num) is the duplicate.
- Walk through indices 0..n-1: the index i where nums[i] > 0 corresponds
  to the missing number i + 1.

Complexities:
- Index Marking: Time O(n), Space O(1) auxiliary (mutates input array).
- Hash Set + Sum Formula: Time O(n), Space O(n) for the set.

--- LEARNING ---
Custom Intuition:
- Sort nums so identical elements sit next to each other, record the
  duplicated value in `dup`, collect unique elements into `num2`, and then
  find which number in 1..n is missing from `num2`.

Errors Encountered & Fixes Along the Way:
1. Confusing index and element value (`for i in nums:`): Treated element
   values as indices or assumed elements were already in 1..n order, causing
   IndexError on [2, 2] and wrong output on unsorted inputs like [3, 2, 2].
2. Assuming the array must stay in 1..n order: Realized mismatch refers to
   one duplicated number and one missing number from 1..n, even when the
   array is shuffled (e.g., [3, 2, 2] -> [2, 1]).
3. Searching for the missing number too early & returning prematurely:
   Checked 1..n inside the `else` branch before finishing the `nums` loop
   and returned on the first candidate, causing [1, 5, 3, 2, 2, 7, 6, 4, 8, 9]
   to return [2, 3] instead of [2, 10].
4. Fix: Track `dup` across the entire loop, finish building `num2`, and only
   then scan range(1, len(nums) + 1) for the missing element.

Complexity Trade-offs vs. Optimal:
- Time: O(n log n) to sort plus O(n * m) from `not in num2` checks on a list
  (up to O(n^2) when scanning range(1, n + 1) against `num2`), which is slower
  than O(n) index marking or hash set lookups.
- Space: O(n) for `num2`, compared to O(1) auxiliary space with index marking.
"""


class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums.sort()
        num2 = []
        dup = -1

        for num in nums:
            if num not in num2:
                num2.append(num)
            else:
                dup = num

        for candidate in range(1, len(nums) + 1):
            if candidate not in num2:
                return [dup, candidate]

        return []
