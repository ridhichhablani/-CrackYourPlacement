class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        zero_row=set()
        zero_col=set()
        rows=len(matrix)
        cols=len(matrix[0])
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j]==0:
                    zero_row.add(i)
                    zero_col.add(j)
        for r in zero_row:
            for i in range(cols):
                matrix[r][i]=0
        for c in zero_col:
            for i in range(rows):
                matrix[i][c]=0
        return matrix
  
