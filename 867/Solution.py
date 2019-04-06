```python
class Solution(object):
    def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        res = [[] for i in range(len(A[0]))]
        n1= len(A)
        n2= len(A[0])
        for i in range (n2):
            for j in range(n1):
                # res[i].append(A[j][i])
                res[j][i] = A[i][j]
        return res
```
```python
class Solution(object):
    def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        return [[A[j][i] for j in range(len(A))] for i in range(len(A[0])) ]
```
```python
import numpy as np
class Solution(object):
    def isMonotonic(self, A):
            """
            :type A: List[int]
            :rtype: bool
            """
            return np.array(A).T
```