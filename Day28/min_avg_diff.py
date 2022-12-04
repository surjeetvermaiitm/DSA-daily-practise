#Link: https://leetcode.com/problems/minimum-average-difference/

class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        n=len(nums)
        suffix=[0]*n
        right_sum=0
        for i in range(n-1,-1,-1):
            suffix[i]=right_sum
            right_sum+=nums[i]
        # print(suffix)
        res=float("inf")
        left_sum=0
        ans=0
        for i in range(0,n,1):
            left_sum+=nums[i]
            left_avg=left_sum//(i+1)
            if i==n-1:
                right_avg=0
            else:
                right_avg=suffix[i]//(n-i-1)
            # print(left_avg,right_avg)
            if abs(left_avg-right_avg)<res:
                ans=i
                res=abs(left_avg-right_avg)
        return ans
            
        
            
            
        