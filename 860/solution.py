```python
class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        if bills[0]!=5:
            return 0
        count={'5': 1, '10': 0, '20': 0}
        for i in range(1,len(bills)):
            if bills[i]==5:
                count['5']+=1
            elif bills[i]==10:
                if count['5']!=0:
                    count['10']+=1
                    count['5']-=1
                else:
                    return 0
            elif bills[i]==20:
                if  count['5']!=0 and count['10']!=0:
                    count['20']+=1
                    count['5']-=1
                    count['10']-=1
                elif count['5']>=3 and count['10']==0:
                    count['20']+=1
                    count['5']-=3
                else:
                    return 0
        return 1
```
