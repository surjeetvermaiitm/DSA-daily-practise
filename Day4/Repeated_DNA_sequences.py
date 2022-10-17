#Link :https://leetcode.com/problems/repeated-dna-sequences/

class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        # in_s=s[0:10]
        # ans=set()
        # for i in range(1,len(s)-9):
        #     if in_s in s[i:]:
        #         # if in_s not in ans:
        #         #     ans.append(in_s)
        #         ans.add(in_s)
        #         in_s=s[i:i+10]
        #     else:
        #         in_s=s[i:i+10]
        # return list(ans)
        
        map={}
        ans=[]
        for i in range(len(s)):
            map[s[i:i+10]]=1+map.get(s[i:i+10],0)
        for k,v in map.items():
            if v>1:
                ans.append(k)
        return ans
            
        