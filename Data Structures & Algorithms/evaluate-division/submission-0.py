class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adjacency_graph = collections.defaultdict(list) # map a --> list of [b,a/b]
        for i,eq in enumerate(equations):
            a,b = eq
            adjacency_graph[a].append([b,values[i]])
            adjacency_graph[b].append([a,1/values[i]])
        #a/b, a--> b
        def bfs(src,target):
            if src not in adjacency_graph or target not in adjacency_graph:
                return -1.0
            q, visit = deque(), set()
            q.append([src, 1.0])
            visit.add(src)
            while q:
                n, w = q.popleft()
                if n == target:
                    return w
                for nei, weight in adjacency_graph[n]:
                    if nei not in visit:
                        q.append([nei, w * weight])
                        visit.add(nei)
            return -1.0
        return [bfs (q[0], q[1]) for q in queries]