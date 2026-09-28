class Solution:

    def can_ship(self, weights: list[int], days: int, cap: int) -> bool:
        days_taken = 1
        load = 0

        for weight in weights:
            if load + weight <= cap:
                load += weight
            else:
                days_taken += 1
                load = weight

        return days_taken <= days

    def shipWithinDays(self, weights: list[int], days: int) -> int:

        low = max(weights)
        high = sum(weights)

        while low <= high:

            mid = (low + high) // 2

            if self.can_ship(weights, days, mid):
                high = mid - 1
            else:
                low = mid + 1

        return low