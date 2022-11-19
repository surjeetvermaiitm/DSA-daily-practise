import collections
from typing import List
class Solution:
    #Function to detect cycle in an undirected graph.
	def isCycle(self, V: int, adj: List[List[int]]) -> bool:
		#Code here
		if len(adj)==0:
		    return False
		visit=set()
		def bfs(src):
    		q=collections.deque([(src,-1)])
    		visit.add(src)
    		while q:
    		    node_tupple=q.popleft()
    		    node=node_tupple[0]
    		    parent=node_tupple[1]
    		    for nbr in adj[node]:
    		        if nbr not in visit:
        		        q.append((nbr,node))
        		        visit.add(nbr)
    		        elif parent!=nbr:
    		            return True
    		return False
    	def dfs(src,parent):
    	    visit.add(src)
    	    for nbr in adj[src]:
    	        if nbr not in visit:
    	            if dfs(nbr,src)==True:
    	                return True
	            elif parent!=nbr:
	                return True
            return False
        for i in range(V):
            if i not in visit:
                if dfs(i,-1)==True:
                    return True
        return False
		