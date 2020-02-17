### 拓扑排序
首先我们根据字典的排序构建一个入度，出度的图。
```python
def buildEdges(self,word1,word2,indegree,outdegree):
        l=min(len(word1),len(word2))
        for i in range(l):
            if word1[i]!=word2[i]:
                outdegree[word1[i]].add(word2[i])
                indegree[word2[i]].add(word1[i])
                break
```  
如果节点不在入度里，证明它就是出度，排在最前面。用一个queue保存这个结果。  
如果这个queue不为空，我们就把排在最前面的节点加在结果中，然后遍历这个节点出度里的节点，在入度里把对应的节点删掉，如果此时入度节点为空，就把这个节点添加在queue里。  
记得在出度里把queue pop的节点删掉。  
```python
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
```  
最后判断， 如果出度不为空， 证明有遗漏的节点， return ""  
否则返回结果。  
```python
if outdegree:
            return ""
        
        return "".join(res)
```