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