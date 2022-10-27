#nk: https://leetcode.com/problems/longest-consecutive-sequence/

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        st=set(nums)
        ans=1
        for x in nums:
            if x-1 not in st:
                window=1
                while x+window in st:
                    window+=1
                    ans=max(ans,window)
        return ans
  