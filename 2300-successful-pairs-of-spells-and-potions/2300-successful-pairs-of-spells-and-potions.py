class Solution:
    def successfulPairs(self, spells: list[int], potions: list[int],success: int) -> list[int]:
        result = []
        potions.sort()
        for i in range(len(spells)):
            count = 0
            left = 0 
            right =  len(potions) - 1
            while left <= right :
                mid =  (left + right)//2
                if spells[i] * potions[mid] >= success:
                    right = mid - 1
                else:
                    left = mid + 1
            count = len(potions) - left
            result.append(count)
        return result


            


        