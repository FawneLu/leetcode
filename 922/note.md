- My Way  
In this way we use two lists to record the even and odd. Then we insert the odd and even lists in A.  
```python
class Solution(object):
    def sortArrayByParityII(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        odd=[]
        even=[]
        for i in range(0,len(A)):
            if A[i]%2==0:
                even.append(A[i])
            else:
                odd.append(A[i])
        print even,odd
        for i in range(0,len(even)):
                A[2*i]=even[i]
        for i in range(0,len(odd)):
                A[2*i+1]=odd[i]
        return A
```  
- Change positions  
We use a loop to change the odd position with even number and even position with odd number.  
```python
class Solution(object):
    def sortArrayByParityII(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        i,j=0,1
        while True:
            if i<len(A) and A[i]%2==0:
                i+=2
            if j<len(A) and A[j]%2==1:
                j+=2
            if i>=len(A) or j>=len(A):
                break
            
            A[i],A[j]=A[j],A[i]
        return A
```
