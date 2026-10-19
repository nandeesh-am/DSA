class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        i = 0
        j = len(numbers) - 1
        while i < j:
            twosum = numbers[i] + numbers[j]
            if twosum == target:
                return [i+1,j+1]
            elif twosum > target:
                j -=1
            else:
                i+=1
        return[-1,-1]
        