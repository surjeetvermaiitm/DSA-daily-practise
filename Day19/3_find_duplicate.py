#Link: https://leetcode.com/problems/find-the-duplicate-number/

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        st=set()
        for i in range(len(nums)):
            for n in nums:
                if n in st:
                    return n
                else:
                    st.add(n)
#             if nums[abs(nums[i])]>0:
#                 nums[abs(nums[i])]=-1*nums[abs(nums[i])]
#             else:
#                 return abs(nums[i])
             
        
        