#Link: https://leetcode.com/problems/even-odd-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return False
        queue=deque()
        queue.append(root)
        level=0
        while queue:
            n=len(queue)
            level_list=[]
            for i in range(n):
                node=queue.popleft()
                if level%2==0:
                    if node.val%2==0:
                        return False
                    else:
                        level_list.append(node.val)
                elif level%2!=0:
                    if node.val%2!=0:
                        return False
                    else:
                        level_list.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if len(level_list)!=len(set(level_list)):
                return False
            if level%2==0 and level_list!=sorted(level_list): 
                return False
            elif level%2!=0 and level_list!=sorted(level_list,reverse=True):
                return False
            level+=1
        return True
                    
                    
                
        