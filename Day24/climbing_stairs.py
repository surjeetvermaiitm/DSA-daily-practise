#Link: https://leetcode.com/problems/climbing-stairs/

class Solution:
    def climbStairs(self, n: int) -> int:
        
        def f(n,memo={}):
            if n==0:
                memo[0]=1
                return 1
            if n==1:
                memo[1]=1
                return 1
            if n not in memo:
                memo[n]=f(n-1)+f(n-2)
                return memo[n]
            return memo[n]
        return f(n)