class Solution:
    def isPalindrome(self, x: int) -> bool:
        y = x
        rev = 0
        if y < 0:
            return False
        while x > 0  :
            last_digite = x % 10
            x = x//10
            rev = (rev*10)+last_digite
        return rev == y
          

        