"""
Problem: 179. Largest Number
Link: https://leetcode.com/problems/largest-number/
Difficulty: Medium

--- EXPECTED / OPTIMAL APPROACH ---
- Pattern: Sorting & Intervals — Custom Sort Keys (Pairwise Concatenation)
- Intuition: For two stringified numbers `a` and `b`, `a` should appear before `b`
  in the final arrangement if and only if `a + b > b + a` (e.g., for `3` and `30`,
  `"330" > "303"`, so `3` comes first; for `3` and `34`, `"343" > "334"`, so
  `34` comes first). Using a custom comparator or sort key with standard sorting
  orders the elements without manually checking every pair. Finally, if the
  joined string starts with `"0"`, the entire list consisted of zeros, so return
  `"0"`.
- Time Complexity: O(n log n) comparisons using standard sorting (each comparison
  concatenates strings of length up to L, the max digit length).
- Space Complexity: O(n) to store the string representations and joined output.

--- LEARNING ---
- Custom Intuition & Loop Logic: Instead of relying on built-in custom sort keys
  or lambdas, this solution uses a straightforward nested-loop pairwise swap
  pass. First, a `for` loop converts each integer in `nums` into a string in
  `strs`. Next, outer loop `i` and inner loop `j` (`i + 1` to `n - 1`) compare
  `strs[j] + strs[i]` against `strs[i] + strs[j]`. Whenever placing `strs[j]`
  before `strs[i]` produces a lexicographically larger string, a `temp` variable
  swaps them in place. After ordering, a loop appends each string to `result`,
  and `if result[0] == "0": return "0"` collapses leading/all zeros to `"0"`.
- Complexity Trade-off vs. Optimal: Comparing all pairs `(i, j)` in nested loops
  always performs O(n^2) concatenation checks (plus string swaps), whereas a
  standard sort with a custom comparator typically performs O(n log n)
  comparisons and is faster on larger inputs. On the positive side, the nested
  loop avoids comparator/key boilerplate and makes the pairwise `a + b` vs.
  `b + a` decision completely explicit.
"""


class Solution(object):

    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        strs = []
        for num in nums:
            strs.append(str(num))

        n = len(strs)
        for i in range(n):
            for j in range(i + 1, n):
                if strs[j] + strs[i] > strs[i] + strs[j]:
                    temp = strs[i]
                    strs[i] = strs[j]
                    strs[j] = temp

        result = ""
        for s in strs:
            result = result + s

        if result[0] == "0":
            return "0"

        return result
