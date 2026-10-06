class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        i = 0
        for j in range(2,len(nums)):
            if nums[i] != nums[j]:
                nums[i+2] = nums[j]
                i += 1
        return i+2
                

        