#Link: https://leetcode.com/problems/make-array-zero-by-subtracting-equal-amounts/

class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        ans=0
        # def min_g0(lst):
        #     min_ele=float("inf")
        #     for i in lst:
        #         if i>0:
        #             min_ele=min(i,min_ele)
        #     return min_ele if min_ele !=float("inf") else 0
        # min_ele=min_g0(nums)
        # while min_ele>0:
        #     ans+=1
        #     for i in range(len(nums)):
        #         if nums[i]>0:
        #             nums[i]-=min_ele
        #     min_ele=min_g0(nums)
        # return ans
        
        #number of unique ele other than 0
        st=set(nums)
        n=len(st)
        ans=n-1 if 0 in st else n
        return ans