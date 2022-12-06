#Link: https://leetcode.com/problems/is-subsequence/submissions/

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        n1=len(s)
        n2=len(t)
        # if n1==0:
        #     return True
        # if n2==0:
        #     return False
        # i=0
        # j=0
        # while j<n2 and i<n1:
        #     if s[i]==t[j]:
        #         i+=1
        #         j+=1
        #     else:
        #         j+=1
        # return i==n1
        def f(n1,n2,memo={}):
            if n1==0:
                return True
            if n2==0:
                return False
            if (n1,n2) in memo:
                return memo[(n1,n2)]
            if s[n1-1]==t[n2-1]:
                memo[(n1,n2)]= f(n1-1,n2-1)
                return memo[(n1,n2)]
            else:
                memo[(n1,n2)]=f(n1,n2-1)
                return memo[(n1,n2)]
        return f(n1,n2)
