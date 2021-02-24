class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = collections.defaultdict(list)
        for pre in prerequisites:
            graph[pre[0]].append(pre[1])
            
        res = []

        visited = [0]*numCourses

        def checkloop(n):
            if visited[n] == -1:
                return False
            if visited[n] == 1:
                return True

            visited[n] = -1
            for j in graph[n]:
                if not checkloop(j):
                    return False

            visited[n] = 1
            res.append(n)
            return True

        for i in range(numCourses):
            if not checkloop(i):
                return []

        return res
        
    def findOrderbfs(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = collections.defaultdict(set)
        todo = {i :set() for i in range(numCourses)}
        
        res=[]

        for pre in prerequisites:
            todo[pre[0]].add(pre[1])
            graph[pre[1]].add(pre[0])

        queue = collections.deque()

        for k,v in todo.items():
            if len(v) == 0:
                queue.append(k)
                res.append(k)

        while queue:
            node = queue.popleft()
            for i in graph[node]:
                todo[i].remove(node)
                if len(todo[i]) == 0:
                    queue.append(i)
                    res.append(i)

            todo.pop(node)

        if not todo:
            return res
        else:
            return []