#Link: https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        l=0
        r=0
        ans=0
        ct=0
        while r<len(nums):
            if nums[r]==1:
                r+=1
            else:
                ct+=1
                while ct>1:
                    if l<len(nums) and nums[l]==0:
                        ct-=1
                    l+=1
                r+=1
            print(l,r,ct,ans)
            ans=max(ans,r-l-1)
            # if ct==0:
            #     ans=max(ans,r-l-1)
            # elif ct==1:
            #     ans=max(ans,r-l-1)
        return ans
                    
                
                
        