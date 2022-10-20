#Link: https://leetcode.com/problems/sum-of-square-numbers/

class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        i=0
        j=int(pow(c,0.5))
        while i<=j:
            ans=i**2+j**2
            if ans==c:
                return True
            elif ans<c:
                i+=1
            else:
                j-=1
        return False
        