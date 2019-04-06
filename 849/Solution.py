```python
class Solution(object):
    def maxDistToClosest(self, seats):
        """
        :type seats: List[int]
        :rtype: int
        """
        res=0
        count=0
        left=0
        right=len(seats)-1
        count_left=0
        count_right=0
        while seats[left]==0:
            count_left+=1
            left+=1
        while seats[right]==0:
            count_right+=1
            right-=1
        count_zero=max(count_right,count_left)
        
        for i in range(len(seats)):
            if seats[i]==0:
                count+=1
                res=max(count,res)
            if seats[i]==1:
                count=0
                
            
        return max((res+1)//2,count_zero)
```  