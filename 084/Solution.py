```python
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.append(0)
        stack=[]
        max_area=0
        for i in range(len(heights)):
            while stack and heights[i]<=heights[stack[-1]]:
                index=stack[-1]
                stack.pop()
                if not stack:
                    w=i
                else:
                    w=i-stack[-1]-1
                max_area = max(max_area,heights[index]*w)
                
            stack.append(i)
        
        return max_area
```