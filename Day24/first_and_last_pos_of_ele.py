#Link: https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # ans=[]
        # n=len(nums)
        # if n==0:
        #     return [-1,-1]
        # l=0
        # h=n-1
        # while l<h:
        #     mid=l+(h-l)//2
        #     if nums[mid]>=target:
        #         h=mid
        #     else:
        #         l=mid+1
        # first_oc=l
        # l=0
        # h=n-1
        # while l<h:
        #     mid=l+(h-l+1)//2
        #     if nums[mid]>target:
        #         h=mid-1
        #     else:
        #         l=mid
        # last_oc=l
        # if nums[first_oc]==target:
        #     ans.append(first_oc)
        # else:
        #     ans.append(-1)
        # if nums[last_oc]==target:
        #     ans.append(last_oc)
        # else:
        #     ans.append(-1)
        # return ans
        l=0
        h=len(nums)-1
        if len(nums)==0:
            return [-1,-1]
        arr=[-1,-1]
        while l<h:
            mid=(l+h)//2
            # print(l,h,mid)
            if nums[mid]>=target:
                h=mid
            else:
                l=mid+1
        fist_occ=l
        l2=0
        h2=len(nums)-1
        while l2<h2:
            mid2=(l2+h2+1)//2
            if nums[mid2]>target:
                h2=mid2-1
            else:
                l2=mid2
        sec_occ=l2
        if nums[fist_occ]==target:
            arr[0]=fist_occ
        if nums[sec_occ]==target:
            arr[1]=sec_occ

        return arr
        
        