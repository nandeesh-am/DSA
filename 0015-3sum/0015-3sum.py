class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
       nums.sort()
       n=len(nums)
       ans=set()
       for i in range(n):
          if i>0 and nums[i] == nums[i-1]:continue
          j=i+1
          k=len(nums)-1
          while j<k:
            sum = nums[i]+nums[j]+nums[k]
            if sum > 0:
                k-=1
            elif sum < 0:
                j+=1
            else:
                treplt = [nums[i],nums[j],nums[k]]
                ans.add(tuple(treplt))
                j+=1
                k-=1
                while j<k and nums[j] == nums[j-1]:
                    j+=1
                while j<k and nums[k] == nums[k+1]:
                    k-=1
       return [list(x) for x in ans]
        

        
        