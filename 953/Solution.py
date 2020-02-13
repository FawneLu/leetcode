```python
class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        if len(words)==1:
            return True
        for i in range(len(words)-1):
            word_1=words[i]
            word_2=words[i+1]
            
            for j in range(min(len(word_1),len(word_2))):
                if word_1[j]!=word_2[j]:
                    if order.index(word_1[j])>order.index(word_2[j]):
                        return False
                    break
            
                else:
                    if len(word_1)>len(word_2):
                        return False
            
        return True
```