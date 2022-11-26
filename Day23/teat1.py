# Helper function for solving 3 partition problem.
# It returns true if there exist three subsets with the given sum
a1=[]
b1=[]
c1=[]
def subsetSum(S, n, a, b, c):
 
    # return true if the subset is found
    if a == 0 and b == 0 and c == 0:
        return True
 
    # base case: no items left
    if n < 0:
        return False
 
    # Case 1. The current item becomes part of the first subset
    A = False
    if a - S[n] >= 0:
        A = subsetSum(S, n - 1, a - S[n], b, c)

        
 
    # Case 2. The current item becomes part of the second subset
    B = False
    if not A and (b - S[n] >= 0):
        B = subsetSum(S, n - 1, a, b - S[n], c)

 
    # Case 3. The current item becomes part of the third subset
    C = False
    if (not A and not B) and (c - S[n] >= 0):
        C = subsetSum(S, n - 1, a, b, c - S[n])
    a1.append(S[n]) if A==True else None
    b1.append(S[n]) if B==True else None
    c1.append(S[n]) if C==True else None
 
    # return true if we get the solution
    return A or B or C
 
 
# Function for solving the 3–partition problem. It returns true if the given
# set `S[0…n-1]` can be divided into three subsets with an equal sum.
def partition(S):
 
    if len(S) < 3:
        return False
 
    # get the sum of all elements in the set
    total = sum(S)
 
    # return true if the sum is divisible by 3 and the set `S` can
    # be divided into three subsets with an equal sum
    return (sum(S) % 3) == 0 and subsetSum(S, len(S) - 1, total//3, total//3, total//3)
 
 
if __name__ == '__main__':
 
    # Input: a set of integers
    S = [7, 3, 2, 1, 5, 4, 8,2,2,2,1]
 
    print(partition(S))
    print(a1)
    print(b1)
    print(c1)
    