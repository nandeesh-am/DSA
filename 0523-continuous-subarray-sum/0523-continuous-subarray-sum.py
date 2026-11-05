class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        prefix = 0
        mp = {0:-1}
        for i in range(len(nums)):
            prefix += nums[i] 
            rem = prefix % k
            if rem in mp:
                if i - mp[rem] >= 2:
                    return True
            else:
                mp[rem] = i
        return False  
        
                