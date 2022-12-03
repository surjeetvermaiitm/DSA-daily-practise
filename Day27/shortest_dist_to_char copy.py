#Link: https://leetcode.com/problems/shortest-distance-to-a-character/

class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        
        # res=[float("inf")]*len(s)
        # for i in range(len(s)):
        #     for j in range(len(s)):
        #         if s[j]==c:
        #             res[i]=min(res[i],abs(i-j))
        # return res
        #approach2
        
        # res=[float("inf")]*len(s)
        # index = [i for i in range(len(s)) if s.startswith(c, i)]
        # for i in range(len(s)):
        #     if s[i]!=c:
        #         for j in index:
        #             res[i]=min(res[i],abs(i-j))
        #     else:
        #         res[i]=0
        # return res
        
        #approach3 last seen from left and right
        
        ind=float("inf")
        res=[0]*len(s)
        for i in range(len(s)):
            if s[i]==c:
                ind=i
            if ind==float("inf"):
                res[i]=float("inf")
            else:
                res[i]=abs(i-ind)
        ind=float("inf")
        for i in range(len(s)-1,-1,-1):
            if s[i]==c:
                ind=i
            if ind==float("inf"):
                continue
            else:
                res[i]=min(res[i],abs(i-ind))
        return res
                