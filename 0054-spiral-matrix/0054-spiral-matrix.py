class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        n=len(matrix)
        m=len(matrix[0])
        row_start= 0 
        row_end = n-1
        colm_start=0
        colm_end=m-1
        ans=[]
        while row_start<=row_end and colm_start<=colm_end:
            for i in range(colm_start,colm_end+1):
                ans.append(matrix[row_start][i])
            row_start+=1
            for j in range(row_start,row_end+1):
                ans.append(matrix[j][colm_end])
            colm_end-=1
            if row_start<=row_end:
              for j in range(colm_end,colm_start-1,-1):
                 ans.append(matrix[row_end][j])
            row_end-=1
            if colm_start<=colm_end:
              for j in range(row_end,row_start-1,-1):
                ans.append(matrix[j][colm_start])
            colm_start+=1
        return ans
              


        