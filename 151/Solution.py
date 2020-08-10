```python 3
class Solution:
    def reverseWords(self, s: str) -> str:
        s_list=s.split()
        res=""
        if len(s_list)==0:
            return ""
        i=0
        j=len(s_list)-1
        while i<j:
            s_list[i],s_list[j]=s_list[j],s_list[i]
            i+=1
            j-=1
        for i in range(len(s_list)-1):
            res=res+str(s_list[i])
            res=res+" "
        res=res+s_list[-1]
        return res
```
class Solution:
    def reverseWords(self, s: str) -> str:
        s += " "
        stack = []
        res = ""
         
        for char in s:
            if char != " ":
                stack.append(char)
            else:
                if not stack:
                    continue
                while stack:
                    res += stack.pop()
                res += " "
            
        return res[::-1][1:]
    
    
    def reverseWords1(self, s: str) -> str:
        s += " "
        word = ""
        res = ""
        
        for char in s:
            if char == " " and word:
                res += word[::-1]
                res += " "
                word = ""
            elif char != " ":
                word += char
                
        return res[::-1][1:]