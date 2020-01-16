### 用Recursion算24点
这道题使用recursion算24点，我们每次把两个数的加减乘除的和与余下的数放在一起判断能不能算出24点就可以。
```python
for i in range (len(nums)):
            for j in range (len(nums)):
                if i!=j:
                    base=[nums[k] for k in range(len(nums)) if k!=j and k!=i]
                    if self.judgePoint24(base+[nums[i]+nums[j]]):return True
                    if self.judgePoint24(base+[nums[i]*nums[j]]):return True
                    if self.judgePoint24(base+[nums[i]-nums[j]]):return True
                    if self.judgePoint24(base+[nums[j]-nums[i]]):return True
                    if nums[i] and self.judgePoint24(base+[nums[j]/nums[i]]):return True
                    if nums[j] and self.judgePoint24(base+[nums[i]/nums[j]]):return True
```