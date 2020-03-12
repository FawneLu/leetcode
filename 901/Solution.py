```python
class StockSpanner:

    def __init__(self):
        self.stack=[(float('inf'),0)]
        self.count=0

    def next(self, price: int) -> int:
        self.count+=1
        while self.stack and self.stack[-1][0]<=price:
            self.stack.pop()
        res=self.count-self.stack[-1][1]
        self.stack.append((price,self.count))
        return res
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
```