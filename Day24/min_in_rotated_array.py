#Link: https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

class Solution:
    def findMin(self, nums: List[int]) -> int:
        n=len(nums)
        l=0
        h=len(nums)-1
        while l<h:
            mid=l+(h-l)//2
            if nums[mid]<nums[n-1]:
                h=mid
            else:
                l=mid+1
        return nums[l]