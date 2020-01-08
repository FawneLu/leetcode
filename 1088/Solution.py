```python
class Solution:
    def confusingNumberII(self, N: int) -> int:
        rotations=[0,1,6,8,9]
        map_rotations={0:0,1:1,6:9,8:8,9:6}
        self.count=0
        def backtrack(check_num,rotation,digits):
            
            if check_num and check_num!=rotation:
                self.count+=1
            
        
            for i in rotations:
                if check_num*10+i>N:
                    break
                else:
                    backtrack(check_num*10+i,map_rotations[i]*digits+rotation,digits*10)
                
        
        
        backtrack(1,1,10)
        backtrack(6,9,10)
        backtrack(8,8,10)
        backtrack(9,6,10)
        
        return self.count
```