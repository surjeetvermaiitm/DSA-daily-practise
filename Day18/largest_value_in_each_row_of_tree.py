#Link: https://leetcode.com/problems/find-largest-value-in-each-tree-row/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if root==None:
            return []
        ans=[]
        q=deque([root])
        while q:
            n=len(q)
            l_ans=-float("inf")
            for i in range(n):
                node=q.popleft()
                l_ans=max(l_ans,node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            ans.append(l_ans)
        return ans
        