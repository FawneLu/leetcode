```python
class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        if endWord not in wordList:
            return []
        wordList=set(wordList)
        layer={}
        layer[beginWord]=[[beginWord]]
        res=[]
        
        while layer:
            newlayer=collections.defaultdict(list)
            for w in layer:
                if w==endWord:
                    return layer[w]
                else:
                    for i in range(len(w)):
                        char='abcdefghijklmnopqrstuvwxyz'
                        for c in char:
                            if c!= w[i]:
                                nextword=w[:i]+c+w[i+1:]
                                if nextword in wordList:
                                    newlayer[nextword]+=[j+[nextword] for j in layer[w]]
                                    
            wordList-=set(newlayer.keys())
            layer=newlayer
        
        return []
```