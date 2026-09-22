class Solution:
    def removeDuplicates(self, nums: List[int] )-> int:
        #duplicants
        if len(nums)==0:
            return 0
        k=1
        for i in range(1,len(nums)):
            if nums[i]!=nums[k-1]:
                k=k+1
            nums[k-1]=nums[i]
        return k

        