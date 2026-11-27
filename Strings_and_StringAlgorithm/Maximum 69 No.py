"""
Problem: 1323. Maximum 69 Number
Difficulty: Easy

--- EXPECTED / OPTIMAL APPROACH ---
Pattern: Greedy (Most-Significant-Digit First) / Place-Value Math
Intuition:
    Changing a single '6' to '9' increases the value by 3 * 10^k, where k is the
    0-indexed place value from the right. To maximize the gain, we greedily flip
    the leftmost '6' (largest k). If there are no '6's, the original number is
    already maximal.

    - String/Greedy pass: Convert to string/list, replace the first '6' with '9',
      and convert back to int.
    - Pure Math pass (O(1) space): Scan digits with a place-value multiplier or
      extract digits to track the highest place value where a 6 appears, then add
      3 * best_place_value to num.

Time Complexity:
    O(d), where d is the number of digits in num (d <= 5 for num <= 10^4).
Space Complexity:
    O(d) for string/list conversion, or O(1) auxiliary space using pure integer math.

--- LEARNING ---
Custom Intuition & Evolution:
    1. Start with the greedy rule: only one flip is allowed, and flipping the
       earliest '6' from the left gives the biggest boost.
    2. Convert num to `list(str(num))` so individual digits can be mutated in
       place before `break`ing out of the loop.
    3. Rebuilding an integer from a list of digits can either join character
       strings directly (`int("".join(num))`) or reconstruct place values
       numerically (`res = res * 10 + digit`).

Mistakes Encountered Along the Way:
    - Comparing a string character against an integer (`num[i] == 6` instead of
      `num[i] == "6"`), which never matched because `str(num)` yields strings.
    - Trying to assign to a string index directly (`num[i] = "9"` on a `str`),
      which raises TypeError because Python strings are immutable.
    - Returning a list instead of an int (e.g., returning `["9", "9", "6", "9"]`
      or `[9, 9, 6, 9]`), causing a type/output mismatch against the expected int.
    - Using invalid unpack syntax in a return statement (`return *num`), which
      causes a SyntaxError.

Complexity Trade-Offs:
    - Both the list-join version and the commented digit-to-int + `res * 10 + digit`
      version run in O(d) time and O(d) space.
    - `int("".join(num))` avoids an extra loop over the list and skips converting
      characters to ints only to reassemble them, keeping the code concise while
      staying in the same O(d) complexity class. A pure integer math approach
      eliminates string/list allocation for true O(1) space.
"""


class Solution(object):
    def maximum69Number(self, num):
        """
        Current accepted implementation: mutate first '6' in list and join.
        :type num: int
        :rtype: int
        """
        num = list(str(num))
        for i in range(0, len(num)):
            if num[i] == "6":
                num[i] = "9"
                break
        return int("".join(num))

    def maximum69NumberWithDigitLoop(self, num):
        """
        Earlier draft with # comments: converts digits to int and builds `res`
        using base-10 place value (`res * 10 + digit`).
        :type num: int
        :rtype: int
        """
        num = list(str(num))
        for i in range(0, len(num)):
            if num[i] == "6":
                num[i] = "9"
                break

        for i in range(0, len(num)):
            num[i] = int(num[i])

        res = 0
        for digit in num:
            res = res * 10 + digit

        return res

    def maximum69NumberOptimalMath(self, num):
        """
        Optimal O(1)-space pure integer math approach: finds the highest place
        value of a '6' digit and adds 3 * place_value.
        :type num: int
        :rtype: int
        """
        temp = num
        place = 1
        add_value = 0

        while temp > 0:
            if temp % 10 == 6:
                add_value = 3 * place
            temp //= 10
            place *= 10

        return num + add_value
