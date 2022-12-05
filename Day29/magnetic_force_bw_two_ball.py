#Link: https://leetcode.com/problems/magnetic-force-between-two-balls/

class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:    
        position.sort()
        n=len(position)
        def f(min_force):
            ans=1
            i=0
            j=1
            while j<n:
                if position[j]-position[i]<min_force:
                    j+=1
                else:
                    ans+=1
                    i=j
                    j+=1
            return ans
        l=1
        h=position[n-1]
        while l<h:
            mid=l+(h-l+1)//2
            # print(l,h,mid,f(mid))
            if f(mid)>=m:
                l=mid
            else:
                h=mid-1
        return l
                
                
                
        