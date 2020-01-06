```python
class Solution:
    def areSentencesSimilarTwo(self, words1: List[str], words2: List[str], pairs: List[List[str]]) -> bool:
        
        if len(words1)!=len(words2):
            return False
        similars=collections.defaultdict(set)
        for word1,word2 in pairs:
            similars[word1].add(word2)
            similars[word2].add(word1)
        
        def dfs(word1,word2,visits):
            for similar in similars[word2]:
                if word1==similar:
                    return True
                elif similar not in visits:
                    visits.add(similar)
                    if dfs(word1,similar,visits):
                        return True
            return False
        
        for w1,w2 in zip(words1,words2):
            if w1!=w2 and not dfs(w1,w2,set([w2])):
                return False
        
        return True
```