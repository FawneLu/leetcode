```python
class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res=[]
        cur=[]
        count=0
        
        for word in words:
            if count+len(word)+len(cur)>maxWidth:
                for i in range(maxWidth-count):
                    cur[i%(len(cur)-1 or 1)]+=' '
                
                res.append(''.join(cur))
                cur=[]
                count=0
            
            cur+=[word]
            count+=len(word)
        
        res.append(' '.join(cur).ljust(maxWidth))
        
        return res
```