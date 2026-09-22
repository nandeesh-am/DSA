class Solution:
    def smallestDivisor(self, nums: list[int], threshold: int) -> int:
        low = 1
        high = max(nums)
        ans = float('inf')
        while low <= high:
            mid = (low + high)//2
            total = 0
            for i in nums:
                total += math.ceil(i/mid)
            if total <=threshold :
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        return int(ans)
        