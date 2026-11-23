"""
Problem: 739. Daily Temperatures
Difficulty: Medium

--- EXPECTED / OPTIMAL APPROACH ---
Pattern: Monotonic Decreasing Stack

Intuition:
Maintain a stack of unresolved day indices whose temperatures stay in
decreasing order. As we iterate through each day (`curr_idx`, `curr_temp`),
any colder unresolved day (`curr_temp > temperatures[stack[-1]]`) has found
its very first strictly warmer day today. Pop `prev_idx` and record the wait
time as `curr_idx - prev_idx`. Push `curr_idx` onto the stack and leave
unresolved days at `0`.

Time Complexity:
- O(n), where n is len(temperatures). Each index is pushed onto the stack once
  and popped at most once.

Space Complexity:
- O(n) in the worst case (strictly decreasing temperatures) for the stack and
  result list.

--- LEARNING ---
Custom Intuition & Loop Attempts:
1. Forward step counting (`days`) & nested `for` loop (`j` in `range(i + 1, n)`):
   - Idea: For each outer day `i`, check future days `j` and increment `days`
     until `temperatures[j] > temperatures[i]`, appending `days` on match or
     `0` if no warmer day is found.
2. What went wrong across earlier attempts & why:
   - Putting `days += 1` inside `if temperatures[j] > temperatures[i]:` only
     incremented on the matching day, making `days` equal to `1` whenever a
     warmer day appeared even after multi-day gaps (e.g., `[75, 71, 69, 72, 76]`
     at `i = 0` would give `1` instead of `4`). Moving `days += 1` outside the
     `if` (at the top of the inner loop) tracks every day stepped forward.
   - Placing `ans.append(0)` outside `for i in range(n):` ran `0` only once
     at the very end instead of once per day when no warmer day was found.
   - Putting `ans.append(0)` right after the inner loop without `else:` or a
     guard caused execution to append `0` even after `break` (producing
     interleaved `0`s like `[1, 0, 1, 0, 4, 0, ...]`).
   - Indenting `else:` at the same level as `if temperatures[j] > temperatures[i]:`
     turned it into an `if ... else` on every single inner iteration rather
     than a `for ... else` (or guarded fallback) for the whole inner loop.
   - Even with clean `for ... else` or `found` handling, nested `for` loops
     take O(n^2) time and hit Time Limit Exceeded on inputs near 10^5 days.
3. Why the monotonic stack (`curr_idx - prev_idx`) works cleanly:
   - Pre-initializing `ans = [0] * n` avoids any `0`-appending / `break` /
     `else` indentation traps.
   - Storing indices rather than temperatures lets us compute wait days
     directly via `curr_idx - prev_idx` in O(1) per pop while keeping total
     runtime at O(n).
"""


class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        Return the number of days to wait after each day for a strictly warmer
        temperature, or 0 if no warmer day occurs in the future.

        Args:
            temperatures: List of daily temperature integers.

        Returns:
            List of wait day counts for each index.
        """
        n = len(temperatures)
        ans = [0] * n
        stack = []

        for curr_idx, curr_temp in enumerate(temperatures):
            while stack and curr_temp > temperatures[stack[-1]]:
                prev_idx = stack.pop()
                ans[prev_idx] = curr_idx - prev_idx
            stack.append(curr_idx)

        return ans



##################################################################################3
# this has higher Time compelxity thus didnt work but is correct code
n = len(temperatures)
        ans = []

        for i in range(n):
            days = 0
            for j in range(i + 1, n):
                days += 1
                if temperatures[j] > temperatures[i]:
                    ans.append(days)
                    break
            else:
                ans.append(0)

        return ans
