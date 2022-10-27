#Link: https://leetcode.com/problems/find-the-smallest-divisor-given-a-threshold/

class Solution:
    def f(self,nums,d):
        ans=0
        for n in nums:
            ans+=ceil(n/d)
        return ans
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        l=1
        h=sum(nums)
        while l<h:
            mid=l+(h-l)//2
            if self.f(nums,mid)<=threshold:
                h=mid
            else:
                l=mid+1
        return l