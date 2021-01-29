#
# https://leetcode.com/problems/valid-palindrome/


class Solution:
    def isPalindrome(self, s: str) -> bool:
        if s == '':
            return True

        s = s.lower()
        # it's now lowercase only
        s = s.strip()
        # remove whitespace at either end
        s = s.replace(' ', '')

        stack = []


        # iterate over each character
        for ch in s:
            # filter out letters only
            is_letter = (ch >= 'a' and ch <= 'z')
            is_number = (ord(ch) >= ord('0') and ord(ch) <= ord('9'))
            if is_letter or is_number:
                stack.append(ch)

        # get midpoint
        mid = len(stack) // 2
        half1 = stack[:mid]
        # if len is odd, then skip exact midpoint, thus
        is_len_odd = len(stack) % 2 == 1
        mid += 1 if is_len_odd else 0
        half2 = stack[mid:]

        # ex:
        # test case: 123321
        # len=6; mid=3
        # 1st: 0,1,2
        # 2nd: 3,4,5

        # iterate

        # test case: 12321
        # len=5; mid=2
        # 1st: 0,1
            #WAS 2nd: 2,3,4
        # 2nd: 3,4

        return half1[::-1] == half2

if __name__ == '__main__':
    # Example 1:
    Input1  = "A man, a plan, a canal: Panama"
    # Output1 = true

    # Example 2:
    Input2  = "race a car"
    # Output2 = false

    soln = Solution()
    print(soln.isPalindrome(Input1))
    print(soln.isPalindrome(Input2))
    print(soln.isPalindrome('taco, cat'))
