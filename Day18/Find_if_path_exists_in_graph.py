#Link: https://leetcode.com/problems/find-if-path-exists-in-graph/

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        
        if source==destination:
            return True
        graph={i:[] for i in range(n)}
        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)
        print(graph)
        visited=set()
        q=deque([source])
        visited.add(source)
        while q:
            node=q.popleft()
            for nbr in graph[node]:
                if nbr==destination:
                    return True
                if nbr not in visited:
                    q.append(nbr)
                    visited.add(nbr)
        return False
            
        
        
        