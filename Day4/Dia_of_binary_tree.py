#Link: https://leetcode.com/problems/diameter-of-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:  
        lh=0
        rh=0
        def diameter_helper(root):
            if root==None:
                return [0,0]
            ld,lh=diameter_helper(root.left)
            rd,rh=diameter_helper(root.right)
            curr_dia=lh+rh
            h=max(lh,rh)+1
            return [max(curr_dia,max(ld,rd)),h]
        
        return diameter_helper(root)[0]  