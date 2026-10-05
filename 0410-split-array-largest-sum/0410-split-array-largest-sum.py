class Solution:
    def countpages(self,nums,pages):
        student = 1 
        pagesstudent = 0
        for i in range(len(nums)):
            if pagesstudent+nums[i] <= pages:
                pagesstudent += nums[i]
            else:
                student += 1
                pagesstudent = nums[i]
        return student



    def splitArray(self, nums: list[int], k: int) -> int:
        low = max(nums)
        high = sum(nums)
        while low <= high:
            mid = (low + high)//2
            countstudent = self.countpages(nums,mid) 
            if countstudent > k:
                low = mid + 1
            else:
                high = mid - 1
        return low






        