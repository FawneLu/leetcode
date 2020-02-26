```python
class Solution:
    def trap(self, height: List[int]) -> int:
        res=0
        current=0
        stack=[]
        while current<len(height):
            while stack and height[current]>height[stack[-1]]:
                top=stack.pop()
                if not stack:
                    break
                distance=current-stack[-1]-1
                bound=min(height[current],height[stack[-1]])-height[top]
                res+=distance*bound
            stack.append(current)
            current+=1
        return res
```
```python
class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        
        max_left=[0]*len(height)
        max_right=[0]*len(height)
        
        max_left[0]=height[0]
        for i in range(1,len(height)):
            max_left[i]=max(max_left[i-1],height[i])
        
        max_right[len(height)-1]=height[len(height)-1]
        for j in range(len(height)-2,-1,-1):
            max_right[j]=max(max_right[j+1],height[j])
        
        res=0
        for i in range(1,len(height)-1):
            res+=min(max_left[i],max_right[i])-height[i]
        
        return res
```