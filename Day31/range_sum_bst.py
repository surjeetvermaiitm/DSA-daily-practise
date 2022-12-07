#Link: https://leetcode.com/problems/range-sum-of-bst/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        #Inorder traversal
        # res=[]
        # def f(root):
        #     if root==None:
        #         return
        #     f(root.left)
        #     res.append(root.val)
        #     f(root.right)
        # f(root)
        # ans=0
        # for n in res:
        #     if n>=low and n<=high:
        #         ans+=n
        # return ans
        ans=0
        def dfs(root):
            nonlocal ans
            if root==None:
                return 
            if root.val>=low and root.val<=high:
                ans+=root.val
            if low<root.val:
                dfs(root.left)
            if root.val<high:
                dfs(root.right)
        dfs(root)
        return ans