class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x < 0 else 1
        x = abs(x)

        s = list(str(x))

        left = 0
        right = len(s) - 1

        while left <= right:
            temp = s[left]
            s[left] = s[right]
            s[right] = temp

            left += 1
            right -= 1

        ans = sign * int(''.join(s))
        if ans < -2**31 or ans > 2**31 - 1:
            return 0
        else:
            return ans