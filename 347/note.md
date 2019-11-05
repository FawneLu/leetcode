- 学会用Counter并对字典进行排序
这道题用了一个Counter来计数list里出现的个数。  
1. Counter(list).most_common(n)可以用来选择前n的value最大的值，储存成[(key 1,value 1),(key 2,value 2),...,(key n,value n)]的形式。
```python3
counter=Counter(nums).most_common(k)
        print(counter)
        res=[]
        for i in range(0,k):
            res.append(counter[i][0])
        return res
```  
2. 我们也要学会对dictionary进行排序。这道题是对value进行排序。  
```python3
counter=Counter(nums)
        sorted_counter=sorted(counter.items(),key=lambda x:x[1], reverse=True )
        res=[]
        for i in range(k):
            res.append(sorted_counter[i][0])
        return res
```
