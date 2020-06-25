### 二分搜索的变形
寻找k个离target最近的数字。  
首先我们利用二分查找找到相邻的两个指针left和right，这两个指针是现在离target最近的两个数。  
```python
while left < right-1:
            mid = left + (right - left)//2
            if arr[mid] <= x:
                left = mid
            else:
                right = mid
```
这边要注意，while循环里写的是能进入循环的条件。当left==right-1的时候已经找到相邻两个了要跳出循环。  
此外，改变left和right的时候，left只能变为mid，right也只能变为mid，因为不缺此时的left和right包不包含在结果里（不是找target，而是找离target最大的数）。  
