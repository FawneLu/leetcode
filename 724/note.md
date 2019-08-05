我失败了，这道题按我的思路来写就是超时，totally不开心，我是傻子。
- 张老师的思路1
先从左到右，再从右到左遍历数组，把他们的累加和放在两个空的list里。把从右到左的那个list反转一下，然后两个比较。这里巧妙的用了一个zip。当累加和相等的时候输出当时的index就可以了。
```python
sum_left=[]
        cum=0
        for num in nums:
            cum+=num
            sum_left.append(cum)
        
        sum_right=[]
        cum=0
        for num in nums[::-1]:
            cum+=num
            sum_right.append(cum)
        sum_right.reverse()
        
        for index,(x,y) in enumerate(zip(sum_left,sum_right)):
            if x==y:
                return index
        return -1
```
- 张老师的思路2
从左到右遍历数组，用一个空的list存放累加和。然后，用总和减去每一个index对应的累加和再加上对应位置的num，跟该index对应的累加和比较。
```python
        cum_num=[]
        cum=0
        for num in nums:
            cum+=num
            cum_num.append(cum)
        for i,c in enumerate(cum_num):
            if c == (cum_num[-1] - c + nums[i]):
                return i
        return -1 
```
