#Link: https://leetcode.com/problems/single-element-in-a-sorted-array/

class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        # ans=0
        # for n in nums:
        #     ans=ans^n
        #     print(ans)
        # return ans
        n=len(nums)
        l=0
        h=n-1
        if n==1:
            return nums[0]
        while l<h:
            mid=l+(h-l+1)//2
            if (mid%2==0 and nums[mid]==nums[mid-1]) or  (mid%2==1 and nums[mid]==nums[mid+1]):
                h=mid-1
            else:
                l=mid
        return nums[l]
        # while l<=h:
        #     mid=(l+h)//2
        #     if nums[mid]!=nums[mid-1] and nums[mid]!=nums[mid+1]:
        #         return nums[mid]
        #     elif (mid%2==0 and nums[mid]==nums[mid-1]) or (mid%2==0 and nums[mid]==nums[mid-1]):
        #         h=mid-1
        #     else:
        #         l=mid
        # return nums[mid]