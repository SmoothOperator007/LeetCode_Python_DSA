"""
Problem: Self Crossing (LeetCode #335)
Difficulty: Hard

--- EXPECTED / OPTIMAL APPROACH ---
- Pattern: Single-Pass Array Scan & Local Geometry / Case Analysis
- Intuition:
  A path moving in alternating 90-degree turns can only self-intersect if the
  current segment `i` meets or crosses a previous segment within 3 to 5 steps
  back (4-line cross, 5-line meet, or 6-line wrap-around cross). Checking just
  these local index relations in one pass detects any crossing as soon as it
  happens.
- Time Complexity: O(n), where n is len(distance).
- Space Complexity: O(1), using only index arithmetic and constant variables.

--- LEARNING ---
- Custom Intuition & Logic:
  Iterates `i` from 3 to len(distance) - 1 because at least 4 segments are
  needed to form a crossing:
  1. `i >= 3` (4-line cross): `distance[i] >= distance[i - 2]` and
     `distance[i - 1] <= distance[i - 3]`.
  2. `i == 4` (5-line meet): `distance[3] == distance[1]` and
     `distance[4] >= distance[2] - distance[0]`.
  3. `i >= 5` (6-line cross): checks inward wrap conditions across `i` down
     to `i - 5` (`distance[i - 3] - distance[i - 5] <= distance[i - 1]`,
     `distance[i - 1] <= distance[i - 3]`,
     `distance[i] >= distance[i - 2] - distance[i - 4]`, and
     `distance[i - 2] > distance[i - 4]`).
- Trade-offs vs. Optimal Way:
  Matches the optimal O(n) time and O(1) space complexity directly. Keeping
  each case explicit makes the index offsets clear, though the `i == 4` check
  is a special case of the general `i >= 4` rule (`distance[i - 1] == distance[i - 3]`
  and `distance[i] >= distance[i - 2] - distance[i - 4]`).
"""


class Solution(object):
    def isSelfCrossing(self, distance):
        """
        :type distance: List[int]
        :rtype: bool
        """
        for i in range(3, len(distance)):
            if (
                distance[i] >= distance[i - 2]
                and distance[i - 1] <= distance[i - 3]
            ):
                return True
            if (
                i == 4
                and distance[3] == distance[1]
                and distance[4] >= distance[2] - distance[0]
            ):
                return True
            if (
                i >= 5
                and distance[i - 3] - distance[i - 5] <= distance[i - 1]
                and distance[i - 1] <= distance[i - 3]
                and distance[i] >= distance[i - 2] - distance[i - 4]
                and distance[i - 2] > distance[i - 4]
            ):
                return True
        return False
