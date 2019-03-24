- Violence Way  
Firstly, we can count the number of '1' in the num. Then we use a violence algorithm to calculate all the possibilities of the time and compare with the num.  
```pyhthon
class Solution(object):
    
    def countBit(self,num):
        count = 0
        while num:
            num &= (num - 1)
            count += 1
        return count
        
    
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        res =[]
        for hour in range(12):
            for minutes in range(60):
                time = "{}:{:02d}".format(hour,minutes)
                if self.countBit(hour)+ self.countBit(minutes) == num:
                    res.append(time)
        return res
```  