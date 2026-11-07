class Solution:
    def arrayRankTransform(self, arr: list[int]) -> list[int]:
        arr_sort = sorted(set(arr))
        rank  = {}
        for i in range(len(arr_sort)):
            rank[arr_sort[i]] = i+1
        result = []
        for nums in arr:
            result.append(rank[nums])
        return result

        