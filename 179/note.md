- Sort也好难 我枯了
这道题注意要用recursion。  
先把一整个list分成几个小的list，先把小的list进行排序之后，再整合成一个list。  
1. 拼接两个数字看哪个在前比较大
```python3
def compare(self,num1,num2):
        if num1+num2>=num2+num1:
            return True
        else:
            return False
```  
2. 将两个list按拼接结果在merge到一起
```python3
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
```  
3. 把list不断切分成两个小的list进行排序（注意recursion）  
```python3
def merge_sort(self,nums):
        if len(nums)<=1:
            return nums

        length=len(nums)

        return self.merge(self.merge_sort(nums[:length//2]),self.merge_sort(nums[length//2:]))
```