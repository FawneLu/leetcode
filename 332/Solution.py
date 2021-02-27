def findItinerary(self, tickets: List[List[str]]) -> List[str]:
    graph= collections.defaultdict(list)
    for fr, to in tickets:
        graph[fr].append(to)
    for fr, to in graph.items():
        to.sort(reverse = True)
    
    res = []
    self.dfs(graph, "JFK", res)
    return res[::-1]

def dfs(self, graph, source, res):
    while graph[source]:
        v = graph[source].pop()
        self.dfs(graph, v, res)
    
    res.append(source)