#Link: https://leetcode.com/problems/squares-of-a-sorted-array/

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # nums.sort(key=lambda x:x*x)
        # res=[]
        # for n in nums:
        #     res.append(n*n)
        # return res
        i=0
        n=len(nums)
        j=n-1
        res=[0]*n
        k=n-1
        while i<=j:
            if abs(nums[i])<=abs(nums[j]):
                res[k]=nums[j]*nums[j]
                k-=1
                j-=1
            else:
                res[k]=nums[i]*nums[i]
                k-=1
                i+=1
        return res