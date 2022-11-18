#Link: https://leetcode.com/problems/ugly-number/

class Solution:
    # def isPrime(self,n):
    #     for i in range(2,ceil(pow(n,0.5))+1):
    #         if n%i==0:
    #             return False
    #     return True
    
    def isUgly(self, n: int) -> bool:
        if n==0:
            return False
        for p in (2,3,5):
            while n%p==0:
                n=n/p
        return n==1
#         n=abs(n)
#         prime = [True for i in range(n+1)]
#         def SieveOfEratosthenes(n):
#             p = 2
#             while (p * p <= n):
#                 if (prime[p] == True):
#                     for i in range(p * p, n+1, p):
#                         prime[i] = False
#                 p += 1
#         SieveOfEratosthenes(n)
#         for i in range(7,int(n/2)+1):
#             if prime[i] and n%i==0:
#                 return False
#         return True
        
        