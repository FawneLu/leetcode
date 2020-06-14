class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        res=n
        father=[i for i in range(n)]
        
        def find(node):
            if father[node]==node:
                return node
            return find(father[node])
            
        def union(node1,node2):
            root_1=find(node1)
            root_2=find(node2)
            if root_1 != root_2:
                father[root_2]=root_1
                return True
            else:
                return False
        
        for node1,node2 in edges:
            if not union(node1,node2):
                return False
        return len(edges)==n-1