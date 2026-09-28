class Solution:
    def findKthPositive(self, arr: list[int], k: int) -> int:
        n=(max(arr)+k)+1
        count = 0
        for i in range(1,n):
            if i not in arr:
                count +=1
                if count == k:
                   return i

        