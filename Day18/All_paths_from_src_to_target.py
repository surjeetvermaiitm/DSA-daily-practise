#Link: https://leetcode.com/problems/all-paths-from-source-to-target/

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        n=len(graph)
        q=deque()
        q.append([0])
        ans=[]

        while q:
            path=q.popleft()
            if path[-1]==len(graph)-1:
                ans.append(path)
            else:
                # q.extend(path+[child] for child in graph[path[-1]])
                for nbr in graph[path[-1]]:
                    q.append(path+[nbr])
    
        return ans
            
        
        