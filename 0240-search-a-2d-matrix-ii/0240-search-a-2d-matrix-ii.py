class Solution:
    def lowerbound(self,mat,n,targt):
        low = 0
        high = n - 1
        ans = -1
        while low <= high:
            mid = (low + high)//2
            if mat[mid] >= targt:
                ans = mat[mid]
                high = mid - 1
            else:
                low = mid + 1
        return ans 

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix)
        m = len(matrix[0])
        for i in range(0,n):
            answer = self.lowerbound(matrix[i],m,target)
            if answer == target:
                return True
                break
        return False
        

        