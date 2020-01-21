```python
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity=capacity
        self.cache=[]
        self.visited=dict()

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        
        self.cache.remove(key)
        self.cache.append(key)
        
        return self.visited[key]

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.visited[key]=value
            self.cache.remove(key)
            self.cache.append(key)
        else:
            if len(self.cache)==self.capacity:
                del_key=self.cache[0]
                self.cache=self.cache[1:]
                del self.visited[del_key]
            self.cache.append(key)
            self.visited[key]=value
            


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
```