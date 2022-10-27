#Link: https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii/submissions/

class Solution:
    def findMin(self, nums: List[int]) -> int:
        n=len(nums)
        l=0
        h=n-1
        if nums[l]<nums[h]:
            return nums[l]
        while l<n and nums[l]==nums[n-1]:
            l+=1
        
        if l>h: 
            return nums[h]
        while l<h:
            mid=l+(h-l)//2
            if nums[mid]>nums[n-1]:
                l=mid+1
            else:
                h=mid
        return nums[l]