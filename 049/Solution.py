```python
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res={}
        
        for word in strs:
            k="".join(sorted(word))
            if k not in res:
                res[k]=[]
            res[k].append(word)
        
        return (res.values())
```