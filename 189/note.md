- First Way (This is the only way I come up with) 
We can use a loop to solve the problem. Everytime we insert the last element to the first position and pop the last one.  
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
- Second Way  
In this way, we can use the way of thinking that we use the k to mod the length of the list, the result is the length that each element in the list need to move.  
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
- Third Way
The third way is the optimization of the second one. We need to pay attention to the difference betwwen 浅copy and 深copy (hhhhh, too low).  
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