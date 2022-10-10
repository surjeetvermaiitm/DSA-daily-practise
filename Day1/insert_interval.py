class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        new_list=[]
        if(len(intervals)==0):
            return [newInterval]
        if (intervals[0][0]>=newInterval[0]):
            new_list.append(newInterval)
        
        for i in range(len(intervals)-1):
            if intervals[i][0]<=newInterval[0] and intervals[i+1][0]>newInterval[0]:
                new_list.append(intervals[i])
                new_list.append(newInterval)
            else:
                new_list.append(intervals[i])
        new_list.append(intervals[-1])
        if(intervals[-1][0]<=newInterval[0]):
            new_list.append(newInterval)
                
        ans=[]  
        curr_interval=new_list[0]
        for next_interval in new_list[1:]:
            if curr_interval[1]>=next_interval[0]:
                # if curr_interval[1]<next_interval[1]:
                #     curr_interval[1]=next_interval[1]
                curr_interval[1]=max(curr_interval[1],next_interval[1])
            else:
                ans.append(curr_interval)
                curr_interval=next_interval
        ans.append(curr_interval)
        return ans
                