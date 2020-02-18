```python
class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        def dfs(l,r,exp,cur,last,res):
            if l==r:
                if cur==target:
                    res.append(exp)
                return
            
            for i in range(l+1,r+1):
                if i==l+1 or (i>l+1 and num[l]!='0'):
                    s,x=num[l:i],int(num[l:i])
                    
                    if last==None:
                        dfs(i,r,s,x,x,res)
                        
                    else:
                        dfs(i,r,exp+'+'+s,cur+x,x,res)
                        dfs(i,r,exp+'-'+s,cur-x,-x,res)
                        dfs(i,r,exp+'*'+s,cur-last+last*x,last*x,res)
        
        res=[]
        dfs(0,len(num),"",0,None,res)
        return res
```

```python
class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        res=[]
        string=" "*(len(num)*2)
        self.dfs(num,target,0,string,0,0,0,res)
        return res
    
    def dfs(self,num,target,pos,string,length,prev,cur,res):
        if pos==len(num):
            if cur==target:
                res.append(string[:length])
            return
        n=0
        s=pos
        l=length
        if (s != 0):
            length+=1
        while pos<len(num):
            n=n*10+int(num[pos])
            if num[s]=='0' and pos-s>0:
                break
            if n>float('inf'):
                break
            new_string=list(string)
            new_string[length]=num[pos]
            string="".join(new_string)
            length+=1
            pos+=1
            if (s == 0):
                self.dfs(num, target, pos, string, length, n, n, res);
                continue
            new_string=list(string)
            new_string[l] = '+'
            string="".join(new_string)
            self.dfs(num, target, pos, string, length, n, cur + n, res)
            new_string=list(string)
            new_string[l] = '-'
            string="".join(new_string)
            self.dfs(num, target, pos, string, length, -n, cur - n, res)
            new_string=list(string)
            new_string[l] = '*'
            string="".join(new_string)
            self.dfs(num, target, pos, string, length, prev * n, cur - prev + prev * n, res)
```