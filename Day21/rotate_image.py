#Link: https://leetcode.com/problems/rotate-image/


class Solution:
  def rotate(self, matrix: List[List[int]]) -> None:
      """
      Do not return anything, modify matrix in-place instead.
      """
      n=len(matrix)
      for row in matrix:
          row.reverse()
          
      for i in range(n):
          for j in range(n-i):
              matrix[i][j],matrix[n-1-j][n-1-i]=matrix[n-1-j][n-1-i],matrix[i][j]
              
      
        

  