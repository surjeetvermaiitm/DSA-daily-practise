#Link: https://leetcode.com/problems/maximum-candies-allocated-to-k-children/

class Solution:
    
    def f(self,max_candies,candies):
        ans=0
        for ele in candies:
            ans+=ele//max_candies
        return ans

    def maximumCandies(self, candies: List[int], k: int) -> int:
        l=0
        h=max(candies)
        mid=0
        while(l<h):
            mid=l+(h-l+1)//2
            # print(f"l {l} h {h} mid {mid} can {self.f(mid,candies)}")
            if self.f(mid,candies)>=k:
                l=mid
            else:
                h=mid-1
        return l