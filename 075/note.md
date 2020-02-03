### 排序
- 用一个dictionary计算每一个数字有几个，然后转换。  
- 设置一个指针cur， index< cur的为0, index> cur 的为2.
```python
while cur<=right:
            if nums[cur]==0:
                nums[cur],nums[left]=nums[left],nums[cur]
                left+=1
                cur+=1
            
            elif nums[cur]==1:
                cur+=1
            
            elif nums[cur]==2:
                nums[cur],nums[right]=nums[right],nums[cur]
                right-=1
```