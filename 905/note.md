- Very Low B Way  
We use two list to record the odd numbers and even numbers. Then we combine the two lists together. We need to pay attention to the difference between append and extend. To decrease the complexity of the space we can use one list and traverse the array twice.  
```python
class Solution(object):
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        
        even=[]
        odd=[]
        for i in range(len(A)):
            if A[i]%2==0:
                even.append(A[i])
            else:
                odd.append(A[i])
                
        even.extend(odd)
        return even
```  
- Not low B way  
We can use one index to record the even. If the number is even then we change the index and the current position and let index plus one.  
```python
class Solution(object):
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """

        index = 0
        for i in range(len(A)):
            if A[i] % 2 == 0:
                A[index],A[i] = A[i],A[index] 
                index += 1
        return A
```
