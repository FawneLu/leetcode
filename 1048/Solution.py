```python
class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words=sorted(words,key=lambda x:len(x))
        def check(str1,str2):
            tmp=""
            for i in range(len(str2)):
                tmp=str2[:i]+str2[i+1:]
                if tmp==str1:
                    return True
            return False
        
        res=[1]*len(words)
        for i in range(len(words)):
            if i>=1 and words[i-1]==words[i]:
                continue
            for j in range(i+1,len(words)):
                if len(words[j])==len(words[i]) or len(words[j])-len(words[i])>1:
                    continue
                if len(words[j])-len(words[i])==1 and check(words[i],words[j]):
                    res[j]=max(res[j],res[i]+1)
        return max(res)
```