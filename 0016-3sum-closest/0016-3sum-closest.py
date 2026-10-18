
class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        closest = nums[0] + nums[1] + nums[2]

        for i in range(n - 2):
            j = i + 1
            k = n - 1

            while j < k:
                sum1 = nums[i] + nums[j] + nums[k]

                if abs(sum1 - target) < abs(closest - target):
                    closest = sum1

                if sum1 == target:
                    return sum1
                elif sum1 < target:
                    j += 1
                else:
                    k -= 1

        return closest


        