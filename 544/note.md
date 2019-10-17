- string和recursion放在一起也让人枯
这道题看起来好烦啊，输出的方法也让人觉得很烦。  
题目很好理解。就是说最强的队要和最弱的队对决。最后输出的结果的是最后的两个对决的队伍。  
```python3
class Solution:
    def findContestMatch(self, n: int) -> str:
        if not n:
            return ""
        
        def helper(x):
            if len(x)==2:
                return "("+x[0]+","+x[1]+")"
            
            return helper(["("
+x[i]+","+x[len(x)-1-i]+")" for i in range (len(x)//2)])
        
        return helper([str(i) for i in range(1,n+1)])
```