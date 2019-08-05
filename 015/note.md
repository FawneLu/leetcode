- 这道题我不会，枯了  
首先我们确定一下two sum的思路。two sum的思路是什么？我们可以先排序，然后两个指针，指向一前一后。如果和小于target，那么左指针往后移一位，如果和大于target，那么右指针往前移一位。这道题求三个数的和，我们只需要现将数组排序，从第一位起开始fix，那么剩下两数的和就是0减fix。不需遍历整个数组，fix到倒数第三位就够了。排序之后，如果数组的第一位是正数也没必要继续算下去，因为和肯定不为0。   
```python
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        nums.sort()
        i=0
        res=[]
        while i<=len(nums)-3:
            if nums[i]>0:
                break
            if i > 0 and nums[i-1] == nums[i]:
                i+=1
                continue
            count=-nums[i]
            left=i+1
            right=len(nums)-1
            while right>left:
                if nums[left]+nums[right]>count:
                    right-=1
                elif nums[left]+nums[right]<count:
                    left+=1
                else:
                    res.append([nums[i],nums[left],nums[right]])
                    while left<right and nums[left]==nums[left+1]:
                        left+=1
                    while left<right and nums[right]==nums[right-1]:
                        right-=1
                            
                    left+=1
                    right-=1
                        
            i+=1
        return res
```
```python
        nums.sort()
        if len(nums)<3 or nums[0]>1 or nums[-1]<0:
            return []
        
        result=[]
        for index,value in enumerate(nums):
            if value>0:
                break
            if index>0 and nums[index]==nums[index-1]:
                continue
            target=-value
            i,j=index+1,len(nums)-1
            while i<j:
                if nums[i]+nums[j]<target:
                    i+=1
                elif nums[i]+nums[j]>target:
                    j-=1
                else:
                    result.append([nums[i],nums[j],value])
                    while i<j and nums[i]==nums[i+1]:
                        i+=1
                    while i<j and nums[j]==nums[j-1]:
                        j-=1
                
                    i+=1
                    j-=1
        
        return result
```