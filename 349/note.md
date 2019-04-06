 - We transform the list into set and judge whether the number in the set nums1 is in the set nums2.  
 ```python
class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nums1=set(nums1)
        nums2=set(nums2)
        res=[]
        for i in nums1:
            if i in nums2:
                res.append(i)
        return res
```  
-  This is the same way of thinking with the fisrt one.  
```python
class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        res=[]
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                if nums1[i]==nums2[j]:
                    res.append(nums1[i])
        return set(res)
```  
- We use '&' to judge whether the two lists have the same value and return the same values in both of the two lists.  
```python
class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        
        return (nums1 & nums2)
```  