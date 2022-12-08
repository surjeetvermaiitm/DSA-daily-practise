#Link: https://leetcode.com/problems/leaf-similar-trees/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        # def dfs(root):
        #     if root==None:
        #         return
        #     if root.left==None and root.right==None:
        #         yield root.val
        #     yield from dfs(root.left)
        #     yield from dfs(root.right)
        # # print(list(dfs(root1)))
        # return list(dfs(root1))==list(dfs(root2))

        def dfs(root,ans):
            if root==None:
                return
            if root.left==None and root.right==None:
                ans.append(root.val)
            dfs(root.left,ans)
            dfs(root.right,ans)
        ans1=[]
        ans2=[]
        dfs(root1,ans1)
        dfs(root2,ans2)
        return ans1==ans2
            