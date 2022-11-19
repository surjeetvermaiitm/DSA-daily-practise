#Link: https://leetcode.com/problems/01-matrix/

#Brute Force
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        rows=len(mat)
        cols=len(mat[0])
        dir=[[-1,0],[1,0],[0,1],[0,-1]]
        ans=[[0]*cols for _ in range(rows)] 
        def dist_f(r,c):
            if mat[r][c]==0:
                return 0
            dist=1
            visit=set([(r,c)])
            q=deque([(r,c)])
            while q:
                n=len(q)
                for i in range(n):
                    node=q.popleft()
                    ro=node[0]
                    co=node[1]
                    for dr,dc in dir:
                        nr=ro+dr
                        nc=co+dc
                        if nr in range(rows) and nc in range(cols) and (nr,nc) not in visit:
                            if mat[nr][nc]==0:
                                return dist
                            else:
                                q.append((nr,nc))
                                visit.add((nr,nc))
                dist+=1
            return dist
               
        for r in range(rows):
            for c in range(cols):
                ans[r][c]=dist_f(r,c)
        return ans
                
            
            
