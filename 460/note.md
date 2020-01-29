### O(1) 实现LFU
用一个ordereddict实现FIFO。  
```python
class Node:
    def __init__(self, key, val, count):
        self.key=key
        self.val=val
        self.count=count
```