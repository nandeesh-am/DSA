class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h={}
        for i in range(len(nums)):
            need=target-nums[i]
            if need in h:
                return[h[need],i] 
            if need not in h:
                h[nums[i]]=i
      

        