#Leetcode: https://leetcode.com/problems/divide-array-into-equal-pairs/

class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        m={n:nums.count(n) for n in nums}
        for k,v in m.items():
            if v%2==1:
                return False
        return True
        