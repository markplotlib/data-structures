# https://leetcode.com/problems/defuse-the-bomb/
class Solution:
    def decrypt(self, code: list, k: int) -> list:
        arr = [0 for i in code]
        i = 0
        h = 0

        if k > 0:
            sign = 1
        elif k < 0:
            sign = -1
        else:
            sign = 0

        while h != len(code):
            j = 0
            sum = 0
            while j != k:
                ind = (i+j+sign) % len(code)
                sum += code[ind]
                j += sign

            ind = (i+j+sign) % len(code)
            arr[sign*h] = sum
            i += sign
            h += 1

        return arr


if __name__ == '__main__':
    sol = Solution()

    code = [5,7,1,4]
    k = 3
    print(sol.decrypt(code=code, k=k))
    # Output: [12,10,16,13]

    code = [2,4,9,3]
    k = -2
    print(sol.decrypt(code=code, k=k))
    # Output: [12,5,6,13]

    code = [1,2,3,4]
    k = 0
    print(sol.decrypt(code=code, k=k))
    # Output: [0,0,0,0]
