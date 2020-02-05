```python
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph=collections.defaultdict(list)
        for pre in prerequisites:
            graph[pre[0]].append(pre[1])
        
        visited=[0]*numCourses
        
        def checkloop(i):
            if visited[i]==1:
                return False
            if visited[i]==2:
                return True
            visited[i]=1
            for j in graph[i]:
                if not checkloop(j):
                    return False
            
            visited[i]=2
            return True
        
        for i in range(numCourses):
            if not checkloop(i):
                return False
            
        return True
```