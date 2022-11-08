#Link: https://leetcode.com/problems/same-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        # def dfs(p,q):
        #     if not p and not q:
        #         return True
        #     if not p or not q:
        #         return False
        #     lans=dfs(p.left,q.left)
        #     rans=dfs(p.right,q.right)
        #     return lans and rans and p.val==q.val
        # return dfs(p,q)
        def BFS(p,q):
            if not p and not q:
                return True
            if not p or not q:
                return False
            q1=deque([p])
            q2=deque([q])
            while q1 and q2:
                node1=q1.popleft()
                node2=q2.popleft()
                if node1.val!=node2.val:
                    return False
                if node1.left and node2.left:
                    q1.append(node1.left)
                    q2.append(node2.left)
                elif node1.left or node2.left:
                    return False
                if node1.right and node2.right:
                    q1.append(node1.right)
                    q2.append(node2.right)
                elif node1.right or node2.right:
                    return False
            return len(q1)==len(q2)
        return BFS(p,q)
        