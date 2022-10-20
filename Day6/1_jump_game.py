#Link: https://leetcode.com/problems/jump-game/

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n=len(nums)
        j=n-1
        for i in range(n-2,-1,-1):
            if nums[i]>=j-i:
                j=i
            #     i-=1
            # else:
            #     i-=1
        return j==0
        