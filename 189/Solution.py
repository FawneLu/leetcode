```python
class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        index=1
        while k:
            nums.insert(0,nums[-1])
            nums.pop(-1)
            #index+=1
            k-=1
        return nums
``` 
```python
def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        mod=k%len(nums)
        res=[]
        for i in range(mod):
            res.append(nums[len(nums)-mod+i])
            nums.pop(len(nums)-mod+i)
        for i in range (len(res)):
            nums.insert(i,res[i])
        return nums
```
```python
def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        l = nums[:]#深拷贝
        #l=nums#浅拷贝
        for i in range(len(nums)):
            nums[(i+k)%len(nums)] = l[i]
        return nums
```