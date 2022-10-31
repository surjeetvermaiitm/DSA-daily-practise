#Link: https://leetcode.com/problems/random-pick-index/

class Solution:

    def __init__(self, nums: List[int]):
        self.nums=nums

    def pick(self, target: int) -> int:
        # r=random.randint(0,len(self.nums)-1)
        # while self.nums[r]!=target:
        #     r=random.randint(0,len(self.nums)-1)
        # return r
        s=0
        e=0
        for i in range(len(self.nums)):
            if self.nums[i]==target:
                s=i
                break
        for i in range(len(self.nums)-1,-1,-1):
            if self.nums[i]==target:
                e=i
                break
        index=random.randint(s,e)
        while self.nums[index]!=target:
            index=random.randint(s,e)
        return index

            
        
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)