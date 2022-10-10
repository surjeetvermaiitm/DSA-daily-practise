class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals=sorted(intervals,key=lambda x: x[0])
        
        curr_interval=intervals[0]
        ans=[]  
        curr_interval=intervals[0]
        for next_interval in intervals[1:]:
            if curr_interval[1]>=next_interval[0]:
                # if curr_interval[1]<next_interval[1]:
                #     curr_interval[1]=next_interval[1]
                curr_interval[1]=max(curr_interval[1],next_interval[1])
            else:
                ans.append(curr_interval)
                curr_interval=next_interval
        ans.append(curr_interval)
        return ans
    
class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals=sorted(intervals,key=lambda x: x[0])
        ans=[intervals[0]]
        
        for x in intervals[1:]:
            prev=ans[-1]
            if prev[1]>=x[0]:
                if prev[1]<x[1]:
                    prev[1]=x[1]
            else:
                ans.append(x)
        return ans
class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals=sorted(intervals,key=lambda x: x[0])
        ans=[intervals[0]]
        
        for x in intervals[1:]:
            prev=ans[-1]
            if prev[1]>=x[0]:
                prev[1]=max(prev[1],x[1])
            else:
                ans.append(x)
        return ans
               