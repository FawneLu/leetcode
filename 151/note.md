- yeah自己写出来了一
For this question, my solution is to cut the string into list. In this step, we delete all the blanks. And next we reverse the list. Lastly we add the elements into the string. Between two elements, there is a blank.
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
