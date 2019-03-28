- Very Low B Way (Maybe) 
This is the way that we use one variable to record the decrease and increase. And then we judge whether the list is mono increase or mono decrease.     
```python
class Solution(object):
    def isMonotonic(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        if len(A)==1:
            return True
        mono=0
        for i in range(0,len(A)-1):
            if A[i+1]-A[i]!=mono:
                mono=A[i+1]-A[i]
                break
                
        if mono>=0:
            for i in range(0,len(A)-1):
                if A[i+1]-A[i]>=0:
                    continue
                else: return False
            return True
        if mono<0:
            for i in range(0,len(A)-1):
                if A[i+1]-A[i]<=0:
                    continue
                else: return False
            return True
```  
- Elegant Way  
We use two variables to record whether the list is increase or decrease. If it is increase then we make the variable which stands for the increase true. If it is decrease then we make the variable which stands for the decrease true. If the two variables are true, then the result is false.  
```python
class Solution(object):
    def isMonotonic(self, A):
            """
            :type A: List[int]
            :rtype: bool
            """
            inc=False
            dec=False
            for i in range(0,len(A)-1):
                if A[i+1]-A[i]>0:
                    inc=True
                if A[i+1]-A[i]<0:
                    dec=True
            return not inc or not dec
```  
- Normal Way  
This way is loop in loop. Runs out of time.  
```python
class Solution(object):
    def isMonotonic(self, A):
            """
            :type A: List[int]
            :rtype: bool
            """
            for i in range(0,len(A)-1):
                if A[i+1]-A[i]>0:
                    for j in range(0,len(A)-1):
                        if A[j+1]-A[j]<0:
                            return False
            return True
```
