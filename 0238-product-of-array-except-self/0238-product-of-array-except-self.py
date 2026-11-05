class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        ans =  [1]*len(nums)
        prefix  = 1
        for i in range(len(nums)):
            ans[i] = prefix
            prefix *= nums[i]
        sufix = 1
        for i in range(len(nums)-1,-1,-1):
            ans[i] = ans[i] * sufix
            sufix *= nums[i]
        return ans


        