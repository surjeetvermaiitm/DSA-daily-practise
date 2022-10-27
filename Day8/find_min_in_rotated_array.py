#Link: https://leetcode.com/problems/find-minimum-in-rotated-sorted-ar

class Solution:
    def findMin(self, nums: List[int]) -> int:
        n=len(nums)
        l=0
        h=n-1
        while l<h:
            mid=l+(h-l)//2
            if nums[mid]>nums[n-1]:
                l=mid+1
            else:
                h=mid
        return nums[l]