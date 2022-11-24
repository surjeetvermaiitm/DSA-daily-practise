#Link: https://practice.geeksforgeeks.org/problems/inversion-of-array-1587115620/1

class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        def merge(arr,l,m,r,temp_arr):    
            mic=0
            i=l
            j=m+1
            k=l
            while i<=m and j<=r:
                if arr[i]<=arr[j]:
                    temp_arr[k]=arr[i]
                    i+=1
                    k+=1
                elif nums[i]>nums[j]:
                    temp_arr[k]=arr[j]
                    mic+=(m-i+1)
                    j+=1
                    k+=1
                    

            while i<=m:
                temp_arr[k]=arr[i]
                i+=1
                k+=1
                
            while j<=r:
                temp_arr[k]=arr[j]
                j+=1
                k+=1
            for m in range(l,r+1):
                arr[m]=temp_arr[m]
            print(arr,mic,l,m,r)
            return mic
      
        def mergesort(arr,l,r,temp_arr):
            ans=0
            if l<r:
                m=l+(r-l)//2
                ans+=mergesort(arr,l,m,temp_arr)
                ans+=mergesort(arr,m+1,r,temp_arr)
                ans+=merge(arr,l,m,r,temp_arr)
            return ans
        temp_arr=[0]*(len(nums))
        res=[]
        for i in range(len(nums)):
            l1=[nums[i:]]
            res.append(mergesort(l1,0,len(nums)-1,temp_arr))
        