```python
class Solution:

    def __init__(self, nums: List[int]):
        self.nums=nums
        

    def pick(self, target: int) -> int:
        index=[]
        for i, num in enumerate(self.nums):
            if num==target:
                index.append(i)
        
        return index[random.randint(0, len(index) - 1)]


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)
```