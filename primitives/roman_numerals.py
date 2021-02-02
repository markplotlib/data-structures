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
        >>> Solution().romanToInt('IV')
        4
        """
        # convert to list
        sum = 0
        s = list(s.lower())
        while len(s) > 0:
            c = s.pop(0)

            # possible subtractors
            if c == 'i':
                if len(s) > 0 and s[0] in 'vx':
                    sum -= 1
                else:
                    sum += 1
            if c == 'x':
                if len(s) > 0 and s[0] in 'lc':
                    sum -= 10
                else:
                    sum += 10
            if c == 'c':
                if len(s) > 0 and s[0] in 'dm':
                    sum -= 100
                else:
                    sum += 100

            # pure additives
            if c == 'v':
                sum += 5
            if c == 'l':
                sum += 50
            if c == 'd':
                sum += 500
            if c == 'm':
                sum += 1000

        return sum
