```python
from collections import Counter
class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        count = Counter(words)
        def compare(x, y):
            if x[1] == y[1]:
                return cmp(x[0], y[0])
            else:
                return -cmp(x[1], y[1])
        return [x[0] for x in sorted(count.items(), cmp = compare)[:k]]

```

```python3
from collections import Counter

class Comparable:
    def __init__(self,key,val):
        self.key = key
        self.val = val
    
    def __lt__(self, Other):
        if self.val < Other.val:
            return True
        elif self.val == Other.val:
            if self.key < Other.key:
                return False
            else:
                return True
        else:
            return False

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        return [cp.key for cp in sorted([ Comparable(key,val) for key,val in Counter(words).items()], reverse = True)[:k]]
```