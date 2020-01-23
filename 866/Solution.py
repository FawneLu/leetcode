```python
class Solution:
    def primePalindrome(self, N: int) -> int:
        def is_prime(n):
            return n>1 and all(n%i for i in range(2,int(n**0.5)+1))
        
        for i in range(1,6):
            for n in range(10**(i-1),10**i):
                n=str(n)
                x=int(n+n[-2::-1])
                if x>=N and is_prime(x):
                    return x
        
        
            for n in range(10**(i-1),10**i):
                n=str(n)
                x=int(n+n[-1::-1])
                if x>=N and is_prime(x):
                    return x
```