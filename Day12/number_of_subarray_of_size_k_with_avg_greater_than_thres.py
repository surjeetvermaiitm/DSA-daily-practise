#Link: https://leetcode.com/problems/number-of-sub-arrays-of-size-k-and-average-greater-than-or-equal-to-threshold/

class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        l=0
        r=0
        avg=0
        ans=0
        for r in range(k):
            avg+=arr[r]/k
      
        if avg>=threshold:
            ans+=1
        for r in range(k,len(arr)):
            avg+=arr[r]/k
            avg-=arr[l]/k
            l+=1
 
            if avg>=threshold:
                ans+=1
        return ans
        