#Link: https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix/

class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        rows=len(grid)
        cols=len(grid[0])
        r=0
        c=cols-1
        ans=0
        while r<rows and c>=0:
            if grid[r][c]<0:
                ans+=(rows-r)
                c-=1
            else:
                r+=1
        return ans
            
        