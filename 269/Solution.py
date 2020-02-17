```python
class Solution:
    def alienOrder(self, words: List[str]) -> str:
        indegree=collections.defaultdict(set)
        outdegree=collections.defaultdict(set)
        zero_indegree=collections.deque()
        nodes=set()
        res=[]
        
        for word in words:
            for c in word:
                nodes.add(c)
        
        
        for i in range(1,len(words)):
            if len(words[i-1])>len(words[i]) and words[i-1][:len(words[i])]==words[i-1]:
                return ""
            self.buildEdges(words[i-1],words[i],indegree,outdegree)
        
        for node in nodes:
            if node not in indegree:
                zero_indegree.append(node)
        
        while zero_indegree:
            pre=zero_indegree.popleft()
            res.append(pre)
            
            if pre in outdegree:
                for c in outdegree[pre]:
                    indegree[c].discard(pre)
                    if not indegree[c]:
                        zero_indegree.append(c)
            
                del outdegree[pre]
        
        if outdegree:
            return ""
        
        return "".join(res)
            
        
        
        
    def buildEdges(self,word1,word2,indegree,outdegree):
        l=min(len(word1),len(word2))
        for i in range(l):
            if word1[i]!=word2[i]:
                outdegree[word1[i]].add(word2[i])
                indegree[word2[i]].add(word1[i])
                break
```
```python
class Solution:
    def alienOrder(self, words: List[str]) -> str:
        nodes=set()
        res=[]
        visited={}
        ancestors=collections.defaultdict(list)
        
        for word in words:
            for c in word:
                nodes.add(c)
                
        for i in range(1,len(words)):
            if len(words[i-1])>len(words[i]) and words[i-1][:len(words[i])]==words[i-1]:
                return ""
            self.buildEdges(words[i-1],words[i],ancestors)
        
        for node in nodes:
            if self.topsortDFS(node,node,ancestors,res,visited):
                return ""
        
        return "".join(res)
            
    def buildEdges(self,word1,word2,ancestors):
        l=min(len(word1),len(word2))
        for i in range(l):
            if word1[i]!=word2[i]:
                ancestors[word2[i]].append(word1[i])
                break
    
    def topsortDFS(self,root,node,ancestors,res,visited):
        if node not in visited:
            visited[node]=root
            for ancestor in ancestors[node]:
                if self.topsortDFS(root, ancestor, ancestors,res,visited):
                    return True
            res.append(node)
            
        elif visited[node]==root:
            return True
        
        return False
```