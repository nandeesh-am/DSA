import math
class Solution:
    def products(self,n,quantities,x):
        stores = 0
        for i in quantities:
            stores += math.ceil(i/x)
        return stores <= n
            
    def minimizedMaximum(self, n: int, quantities: list[int]) -> int:
        low = 1
        high = max(quantities)+1
        while low <= high:
            mid = (low+high)//2
            if self.products(n,quantities,mid):
                high = mid - 1
            else:
                low = mid + 1
        return low



        