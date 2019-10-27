```python3
class Solution:
    def compare(self,num1,num2):
        if num1+num2>=num2+num1:
            return True
        else:
            return False
        
    def merge(self,list1,list2):
        p1,p2=0,0
        result=[]
        while p1<len(list1) and p2<len(list2):
            if self.compare(list1[p1],list2[p2]):
                result.append(list1[p1])
                p1+=1
            else:
                result.append(list2[p2])
                p2+=1
            
        result+=list1[p1:]
        result+=list2[p2:]
        
        return result
        
    def merge_sort(self,nums):
        if len(nums)<=1:
            return nums

        length=len(nums)

        return self.merge(self.merge_sort(nums[:length//2]),self.merge_sort(nums[length//2:]))
    
    def largestNumber(self, nums: List[int]) -> str:
        
        if not any(nums):
            return "0"
        
        nums = list(map(str,nums))
        
        
        return "".join(self.merge_sort(nums))
```