class Solution:
    def maxnum(self,matrx,n,col):
       maxelem = -1
       index = -1
       for i in range(n):
          if matrx[i][col] > maxelem :
            maxelem = matrx[i][col]
            index = i
       return index
    def findPeakGrid(self, mat: list[list[int]]) -> list[int]:
       low = 0
       m = len(mat[0])
       high = m - 1
       n = len(mat)
       while low <= high:
        mid = (low+high)//2
        row = self.maxnum(mat,n,mid)
        if mid  > 0:
            left = mat[row][mid-1]
        else:
            left = -1
        if mid + 1 < m:
            right = mat[row][mid + 1]
        else:
            right = -1
        if mat[row][mid] > left and mat[row][mid] > right:
            return [row,mid]
        if mat[row][mid] > left:
            low = mid + 1
        else: 
            high = mid - 1
       return [-1,-1]

      
    
        