class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sum1=0
        n=len(nums)
        maxm=float('-inf')
        for i in range(n):
            sum1+=nums[i]
            
            if sum1 > maxm:
                maxm = sum1
            if sum1 < 0:
                sum1=0
        return maxm

        
                
        