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