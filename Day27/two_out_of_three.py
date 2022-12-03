#Link: https://leetcode.com/problems/two-out-of-three/

class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        # st1=set(nums1)
        # st2=set(nums2)
        # st3=set(nums3)
        # res=[]
        # for n in nums1:
        #     if n in st2 or n in st3:
        #         res.append(n)
        # for i in nums2:
        #     if (i in st3) and (i not in st1):
        #         res.append(i)
        # return list(set(res))
        
        # approach2
        res=[]
        l1=[0]*101
        l2=[0]*101
        l3=[0]*101
        for i in range(len(nums1)):
            l1[nums1[i]]=1
        for i in range(len(nums2)):
            l2[nums2[i]]=1
        for i in range(len(nums3)):
            l3[nums3[i]]=1
        for i in range(1,101):
            if (l1[i]+l2[i]+l3[i]>=2):
                res.append(i)
        return res
        