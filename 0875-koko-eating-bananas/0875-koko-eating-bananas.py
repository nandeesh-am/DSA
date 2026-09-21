import math
class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        low = 1
        high = max(piles)
        ans = high
        while low <= high:
            mid = (low + high)//2
            total = 0
            for i in piles:
                total += math.ceil(i/mid)
            if total <= h:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        return int(ans)



        