class Solution:
    def minDays(self, bloomDay: list[int], m: int, k: int) -> int:
        n = len(bloomDay)
        if m*k > n:
            return -1
        low = min(bloomDay)
        high  = max(bloomDay)
        while low <= high:
            mid = (low + high)//2
            flower = 0
            bouquet = 0
            for day in bloomDay:
                if day <= mid:
                    flower += 1
                    if flower == k:
                         bouquet += 1
                         flower = 0
                else:
                    flower = 0
            if  bouquet >= m:
                high = mid - 1
            else:
                low = mid + 1
        return low  






        

        
        