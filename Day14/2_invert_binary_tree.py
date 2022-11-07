#Link: https://leetcode.com/problems/invert-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        #DFS
#         if root==None:
#             return None
#         root.left,root.right=root.right,root.left
#         self.invertTree(root.left)
#         self.invertTree(root.right)

#         return root
        #BFS
        if root ==None:
            return None
        q=deque([root])
        while q:
            node=q.popleft()
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
            node.left,node.right=node.right,node.left
        return root
        