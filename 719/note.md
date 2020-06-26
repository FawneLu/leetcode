### 二分查找+双指针
首先确定二分的两个边界。将数组重新排序后，最小值就是第一个数，最大值就是最后一个数减第一个数的差值。  
每次更新mid之后，再用helper函数寻找两个数的差值小于等于mid的个数。  
如果个数小于k，证明找的mid太小，要改变left，否则改变right。  
注意helper函数就是用了一个forward pointer的写法。  
```python
def helper(mid):
            i,count = 0,0
            for j in range(len(nums)):
                while nums[j] - nums[i] > mid:
                    i+=1
                count += j-i
            return count
```