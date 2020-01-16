```python
class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        j,stack=float('-inf'),[]
        for num in nums[::-1]:
            if num <j:return True
            while stack and stack[-1] < num:j=stack.pop()
            stack.append(num)
        return False
```