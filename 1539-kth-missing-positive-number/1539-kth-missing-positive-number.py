class Solution:
    def findKthPositive(self, arr: list[int], k: int) -> int:
         low = 0
         high = len(arr) - 1
         while low <= high:
            mid = (low + high)//2
            messing = arr[mid] - (mid+1)
            if messing < k:
                low = mid + 1
            else:
                high = mid - 1
         return low + k

        