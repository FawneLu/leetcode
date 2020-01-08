```python
class Solution(object):
    def expressiveWords(self, S, words):
        def RLE(S):
            return zip(*[(k,len(list(g))) for k,g in itertools.groupby(S)])
        
        R,count=RLE(S)
        res=0
        
        for word in words:
            R2,count2=RLE(word)
            if R!=R2:continue
            valid=True
            
            for i in range(len(count)):
                if count[i]<count2[i] or (count[i]<3 and count[i]!=count2[i]) :
                    valid=False
                    break
                if count[i]>=3 or count[i] == count2[i]:
                    continue
                
                    
            if valid: res+=1
                
        return res
```