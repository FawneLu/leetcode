### 这算是什么类型的题呢
先求出每个坐标i 左边最高的bar和右边最高的bar。  
res+=min(max_left[i], max_right[i])-height[i]
### stack
stack用来存index。我们最后要得到一个单调递增的栈
Use stack to store the indices of the bars.
Iterate the array:
```python
 while stack and height[current]>height[stack[-1]]:
    			top=stack.pop()
                if not stack:
                    break
                distance=current-stack[-1]-1
                bound=min(height[current],height[stack[-1]])-height[top]
                res+=distance*bound
            stack.append(current)
            current+=1
```
注意bound，如果stack不为空，证明在stack中,top的左边，即stack[-1]一定是一个height比height[top]高的index，此时current和这个index能围成的水的横向高度就是min(height[current],height[stack[-1]])-height[top]