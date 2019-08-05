- 我太捞了
这道题终于被我写出来了...我好蠢...这道题我的思路是这样的。首先我们有个字典用来放钱，然后我们就判断下一次来的钱能不能找。注意，如果别人付20块的话是不是要多考虑一点。是找一个5块一个10块，还是找3个5快呢
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
