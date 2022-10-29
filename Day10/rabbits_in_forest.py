#Link:https://leetcode.com/problems/rabbits-in-forest/

class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        # dt={}
        # for n in answers:
        #     dt[n]=1+dt.get(n,0)
        # ans=0
        # for k,v in dt.items():
        #     if k==0:
        #         ans+=v
        #     else:
        #         if v%(k+1)==0:
        #             ans+=(k+1)*(v//(k+1))
        #         else:
        #             ans+=(k+1)*(v//(k+1))+(k+1)
        #     print(ans)
        # return ans
        dt={}
        for n in answers:
            dt[n]=1+dt.get(n,0)
        ans=0
        for k,v in dt.items():
            ans+=(k+1)*(ceil(v/(k+1)))
        return ans