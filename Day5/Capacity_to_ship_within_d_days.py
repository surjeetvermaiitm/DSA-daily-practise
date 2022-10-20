#Link: https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/

class Solution:
    def f(self,cap,weights):
        ans=0
        cap_so_far=cap
        for w in weights:
            if cap_so_far-w>0:
                cap_so_far-=w
            else:
                ans+=1
                cap_so_far=cap
                cap_so_far-=w
        return ans
            
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l=max(weights)
        h=sum(weights)
        while l<h:
            mid=l+(h-l+1)//2
            #print(f"l {l} h {h} mid {mid} day {self.f(mid,weights)}")
            if self.f(mid,weights)>=days:
                l=mid
            else:
                h=mid-1
        return l