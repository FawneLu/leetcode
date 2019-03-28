- My Way  
In this way we use a list to record the index of the character and then use loop to record the minium distance.  
```python
class Solution(object):
    def shortestToChar(self, S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """
        res=[]
        point=[]
        for i in range(0,len(S)):
            if S[i]==C:
                point.append(i)
        print point
        for i in range(0,len(S)):
            count=abs(i-point[0])
            for j in range(0,len(point)):
                if abs(i-point[j])<count:
                    count=abs(i-point[j])
            res.append(count)
        return res
```  
