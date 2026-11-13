"""Problem Name: 41. First Missing Positive
Difficulty: Hard

--- EXPECTED / OPTIMAL APPROACH ---
Pattern: Cyclic Sort / In-Place Index Placement
Intuition: 
For an array of length n, the first missing positive integer must fall within the range [1, n + 1]. 
We can achieve O(n) time and O(1) space by iterating through the array and swapping each number `x` 
(where 1 <= x <= n) to its correct 0-indexed position (`x - 1`). After the rearrangement, a second 
linear scan identifies the first index where `nums[i] != i + 1`, which reveals the missing positive. 
If all positions match, the answer is `n + 1`.

Complexity:
- Time Complexity: O(n) - Each number is placed in its correct position in at most one swap.
- Space Complexity: O(1) - In-place manipulation without extra data structures.

--- LEARNING ---
Custom Approach & Intuition:
Your solution sorts the array in O(n log n) time and scans through it linearly while tracking `tar = 1`. 
- Skipping elements smaller than `tar` handles duplicates, zeros, and negative numbers gracefully.
- When `i == tar`, you increment the target, and the moment `i > tar`, you immediately spot the missing gap and return `tar`.
- This code is highly readable, intuitive, and cleanly handles edge cases.

Trade-offs:
- Time Complexity: O(n log n) due to the sorting step, which is slightly suboptimal compared to the O(n) cyclic sort but runs well within time limits (achieving 0 ms / fast runtimes on LeetCode).
- Space Complexity: O(1) extra space, matching the optimal constraint.
"""


class Solution(object):

  def firstMissingPositive(self, nums):
    """:type nums: List[int]

    :rtype: int
    """
    nums.sort()
    tar = 1

    for i in nums:
      if i < tar:
        continue
      elif i == tar:
        tar += 1
      else:
        return tar

    return tar
