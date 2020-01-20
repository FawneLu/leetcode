### Krusal最小生成树
构建虚拟节点0，将wells数组转化为每一个村庄1~n与0的边, 然后append到pipes中，对pipes进行排序。    
然后查找村庄x与村庄y分别能到达哪个村庄。  
用一个graph来存储每个村庄到达的最近的村庄。  

```python
def find(i):
            while i!=graph[i]:
                i=graph
```
为了不超时，设一个count。如果x!=y, count+1, 如果count==n则返回res