```python
class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        res=[]
        substring=""
        for s in searchWord:
            substring+=s
            cur=[]
            for word in products:
                if word[:len(substring)]!=substring:
                    continue
                cur.append(word)
            cur=sorted(cur)
            if cur:
                res.append(cur[:3])
            else:
                res.append([])
        return res
```