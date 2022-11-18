#Link: https://leetcode.com/problems/sum-of-square-numbers/

class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        n=int(pow(c,0.5))+1
        i=0
        j=n
        while i<=j:
            if i*i+j*j==c:
                return True
            elif i*i+j*j>c:
                j-=1
            else:
                i+=1
        return False
        