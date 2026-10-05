class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:
        arr1 = []
        arr2 = []
        arr1.append(nums[0])
        arr2.append(nums[1])
        p1 = 0
        p2 = 0
        for i in range(2,len(nums)):
            if arr1[p1] > arr2[p2] :
                arr1.append(nums[i])
                p1 += 1
            else:
                arr2.append(nums[i])
                p2 += 1
        return arr1 + arr2 
        