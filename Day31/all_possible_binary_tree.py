#Link: https://leetcode.com/problems/all-possible-full-binary-trees/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:

        def f(n,memo={}):
            ans=[]
            if n<1 or n%2==0:
                return []
            if n in memo:
                return memo[n]
            if n==1:
                ans.append(TreeNode(0))
                memo[1]=ans
                return ans
            for i in range(1,n,2):
                left=f(i)
                right=f(n-1-i)
                for j in range(len(left)):
                    for k in range(len(right)):
                        root=TreeNode(0)
                        root.left=left[j]
                        root.right=right[k]
                        ans.append(root)
            memo[n]=ans
            return ans
            
        return f(n)
        
