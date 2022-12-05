#Link: https://leetcode.com/problems/search-a-2d-matrix/

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m=len(matrix)
        n=len(matrix[0])
        # def search(arr,l,h):
            
        #     while l<h:
        #         mid=(l+h+1)//2
        #         if arr[mid]>target:
        #             h=mid-1
        #         else:
        #             l=mid
                
        #     return (arr[l]==target) 

        # for i in range(m):
        #     if search(matrix[i],l=0,h=len(matrix[i])-1):
        #         return True
        # return False
        # i=0
        # j=n-1
        # while i<m and j>=0:
        #     if matrix[i][j]==target:
        #         return True
        #     elif matrix[i][j]>target:
        #         j-=1
        #     else:
        #         i+=1
        # return False
        l=0
        h=m*n-1
        while l<h:
            mid=(l+h+1)//2
            r= mid//n
            c= mid%n
            if matrix[r][c]>target:
                h=mid-1
            else:
                l=mid
        r=l//n
        c=l%n
        return (matrix[r][c]==target)