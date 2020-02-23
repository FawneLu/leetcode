```python
class Solution:
    def kthGrammar(self, N: int, K: int) -> int:
        if K==1:
            return 0
        if K<=2**(N-2):
            return self.kthGrammar(N-1,K)
        else:
            return 1-self.kthGrammar(N-1,K-2**(N-2))
```