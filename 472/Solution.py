```python
class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        res=[]
        new_words=set(words)
        for word in words:
            if word=="":
                continue
            new_words.remove(word)
            dp=[0]*(len(word)+1)
            dp[0]=1
            for i in range(len(word)+1):
                for j in range(i):
                    if dp[j]==1 and word[j:i] in new_words:
                        dp[i]=1
                        break
            if dp[-1]==1:
                res.append(word)
            new_words.add(word)
        
        return res
```