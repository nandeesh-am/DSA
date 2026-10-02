class Solution:
    def singleNumber(self, nums: List[int]) -> int:
      h={}
      for i in nums:
        if i in h:
            h[i]+=1
        else:
            h[i]=1
      for key,value in h.items():
        if value==1:
           return key
        