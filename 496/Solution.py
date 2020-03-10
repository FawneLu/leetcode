```python
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dic=dict()
        stack=[]
        for num in nums2:
            while stack and stack[-1]<num:
                dic[stack.pop()]=num
            stack.append(num)
        return [dic.get(i,-1) for i in nums1]
            
    
    
    def nextGreaterElement2(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res=[]
        for num1 in nums1:
            flag=False
            for num2 in nums2:
                if num1==num2:
                    flag=True
                elif flag and num2>num1:
                    res.append(num2)
                    break
            else:
                res.append(-1)
            
        return res
            
    
    
    def nextGreaterElement1(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack=[]
        next_large=[-1]*len(nums2)
        res=[]
        stack.append(0)
        for i in range(len(nums2)):
            while stack and nums2[stack[-1]]<nums2[i]:
                index=stack.pop()
                next_large[index]=nums2[i]
            stack.append(i)
        
        for num in nums1:
            index=nums2.index(num)
            res.append(next_large[index])
            
        return res
```