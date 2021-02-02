# https://leetcode.com/problems/roman-to-integer/
# python -m doctest roman_numerals.py

class Solution:
    def romanToInt(self, s: str) -> int:
        """
        Constraints:
        * 1 <= s.length <= 15
        * s contains only the characters ('I', 'V', 'X', 'L', 'C', 'D', 'M').
        * It is guaranteed that s is a valid roman numeral in the range [1, 3999].

        Assumptions:
        * only correct expressions are passed in

        >>> Solution().romanToInt('III')
        3
        >>> Solution().romanToInt('V')
        5
        """
        # convert to list
        sum = 0
        s = list(s.lower())
        while len(s) > 0:
            c = s.pop(0)
            if c == 'i':
                sum += 1
            if c == 'v':
                sum += 5
            prev = c

        return sum
