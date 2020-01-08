```python
class Solution:
    def confusingNumber(self, N: int) -> bool:
        rotations=[0,1,6,8,9]
        nums=str(N)
        res=""
        for num in nums:
            if int(num) not in rotations:
                return False
            else:
                if num=="6":
                    num="9"
                elif num=="9":
                    num="6"
                res+=num
        return not int(res[::-1])==N
```