### DFS
首先，我们用一个图来存储每一个石头，与它行相同或者列相同的石头。
```python
 graph=collections.defaultdict(list)
        for i,x in enumerate(stones):
            for j in range(i):
                y=stones[j]
                if x[0]==y[0] or x[1]==y[1]:
                    graph[i].append(j)
                    graph[j].append(i)
```  
对于每一块石头来说，从它可以走到n个石头，我们用一个stack来存储这些石头，没访问过的石头，把它的状态变为True，然后放到stack中。如果stack不为0，此时结果+1, 一直访问这块石头可以到的石头放在stack中, 并将访问过的石头的状态变为1。  
直到stack为空时, 结果减1, 不算起始的这块石头。
```python
 N=len(stones)
        res=0
        visited=[False]*N
        
        for i in range(N):
            if not visited[i]:
                stack=[i]
                visited[i]=True
                while stack:
                    res+=1
                    node=stack.pop()
                    for n in graph[node]:
                        if not visited[n]:
                            stack.append(n)
                            visited[n]=True
                
                res-=1
```