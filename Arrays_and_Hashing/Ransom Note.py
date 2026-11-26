"""
Problem: 383. Ransom Note 
Difficulty: Easy

--- EXPECTED / OPTIMAL APPROACH ---
Pattern: Hash Map / Frequency Counting
Intuition:
    Each character in `magazine` can be used at most once to construct `ransomNote`.
    Count how many times each character appears in `magazine`. Then scan `ransomNote`:
    if a character is not present or its available count is already 0, return False.
    Otherwise, decrement its count by 1. If all characters are matched, return True.

Time Complexity: O(m + n), where m is len(magazine) and n is len(ransomNote).
Space Complexity: O(1) — at most 26 lowercase English letters are stored in the map.

--- LEARNING ---
Custom Intuition & Variable Logic:
    - Used `counter = {}` to record frequency counts across `magazine` (`counter[c] += 1` if present, else `counter[c] = 1`).
    - Iterated through `char` in `ransomNote`:
        1. `if char not in counter:` -> no usable occurrences left, so return `False`.
        2. `elif counter[char] == 1:` -> `del counter[char]` removes the key once its last copy is consumed, so subsequent checks cleanly hit `char not in counter`.
        3. `else:` -> `counter[char] -= 1` consumes one occurrence while keeping remaining copies tracked.
    - Returning `True` after the loop confirms every character in `ransomNote` was matched.

Approaches Tried & Why They Didn't Work / Had Trade-offs:
    1. `set(ransomNote) in set(magazine)`:
       - Failed for two reasons: `in` checks element membership rather than subset containment (a `set` object isn't an element inside a set of single-char strings), and `set(...)` discards duplicate counts (e.g., `"aa"` vs `"ab"`).
    2. Loop checking `for i in set(ransomNote): if i in magazine`:
       - Collapsed `"aa"` into `{'a'}` and only checked whether `'a'` existed anywhere in `"ab"`, returning `True` even when two `'a'`s were required.
    3. Calling `sorted(...)` (`magazine.sorted()`):
       - Raised `AttributeError` because `sorted()` is a built-in function, not a string method; also sorting adds $O(m \log m + n \log n)$ overhead when linear counting suffices.
    4. Mutating strings via `magazine = magazine.replace(i, "")` inside a loop:
       - Without a count limit, `.replace(i, "")` strips *all* occurrences of `i` at once (wiping out both `'a'`s in `"aab"` on the first pass and failing the second `'a'`). Even with `replace(i, "", 1)`, repeated string scans/recreations can degrade toward $O(n \cdot m)$ on long inputs up to $10^5$ characters.

Why This Final Code Works Best:
    - Handles duplicate characters accurately by tracking exact counts per character.
    - Runs in $O(m + n)$ time without repeated full-string scans or string copying.
    - Uses $O(1)$ auxiliary space (at most 26 letters) and passes all 131/131 test cases cleanly.
"""


class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        counter = {}
        for c in magazine:
            if c in counter:
                counter[c] += 1
            else:
                counter[c] = 1

        for char in ransomNote:
            if char not in counter:
                return False
            elif counter[char] == 1:
                del counter[char]
            else:
                counter[char] -= 1

        return True
