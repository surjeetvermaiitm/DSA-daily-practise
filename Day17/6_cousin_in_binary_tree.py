#Link: https://leetcode.com/problems/cousins-in-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        if root==None:
            return False
        q=deque([root])
        while q:
            n=len(q)
            isX=False
            isY=False
            for i in range(n):
                node=q.popleft()
                if node.val==x:
                    isX=True
                if node.val==y:
                    isY=True
                if node.left and node.right:
                    if (node.left.val==x and node.right.val==y):
                        return False
                    if (node.right.val==x and node.left.val==y):
                        return False
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            if isX and isY:
                return True
        return False
                    
                        
                
                    
                
                
                
                
                
        
        
        