"""
Problem Name: String to Integer (atoi)
Difficulty: Medium

--- EXPECTED / OPTIMAL APPROACH ---
Optimal Pattern: Single-Pass Iterative Scan with State/Sign Tracking
Intuition:
Iterate through the string index by index, skipping leading whitespace, capturing 
the optional sign (+ or -), accumulating valid digit characters into an integer 
accumulator on the fly, and checking for 32-bit integer boundary overflow/underflow 
at every step. This avoids unnecessary string creation and memory allocations.
Time Complexity: O(n) where n is the length of the string.
Space Complexity: O(1) auxiliary space.

--- LEARNING ---
Custom Intuition & Logic:
- Handled whitespace removal cleanly using `.lstrip(' ')` on the string to manage 
  the leading blanks condition.
- Isolated the sign handling and separated valid digit sequences by looping 
  sequentially and breaking early upon hitting non-digit characters.
- Used a custom dictionary lookup mapping characters ('0'-'9') to integers 
  instead of forbidden built-in functions like `int()`.
- Implemented explicit string slicing and `.lstrip('0')` to clean up 
  extraneous leading zeros safely before manual base-10 accumulation.
Trade-offs:
Using built-in string helper methods and building secondary string allocations 
slightly increases memory overhead compared to a pure single-pointer integer accumulator, 
but maintains high readability and clear modular separation of parsing rules.
"""


class Solution(object):

  def myAtoi(self, s):
    """:type s: str

    :rtype: int
    """
    nums = {
        '0': 0,
        '1': 1,
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9,
    }

    b = s.lstrip(' ')
    if not b:
      return 0

    c = ''
    if b[0] == '-' or b[0] == '+':
      c += b[0]
      for i in b[1:]:
        if i in nums:
          c += i
        else:
          break
    else:
      for i in b:
        if i in nums:
          c += i
        else:
          break

    if c == '' or c == '-' or c == '+':
      return 0

    sign = ''
    digits = c
    if c[0] == '-' or c[0] == '+':
      sign = c[0]
      digits = c[1:]

    digits = digits.lstrip('0')
    if not digits:
      return 0

    res = 0
    for i in digits:
      res = res * 10 + nums[i]

    if sign == '-':
      res = -res

    INT_MIN = -(2**31)
    INT_MAX = 2**31 - 1

    if res < INT_MIN:
      return INT_MIN
    if res > INT_MAX:
      return INT_MAX

    return res
