class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        father=[i for i in range(n)]
        self.res = n
        
        def find(node):
            if father[node]==node:
                return node
            father[node]=find(father[node])
            return father[node]

        def union(node1,node2):
            root_1=find(node1)
            root_2=find(node2)
            if root_1!=root_2:
                father[root_1]=root_2
                self.res-=1
        
        for i,j in edges:
            union(i,j)
        
        return self.res