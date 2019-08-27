```python3
class Solution:
    def validPalindrome(self, s: str) -> bool:
        left=0
        right=len(s)-1
        while left<right:
            if s[left]==s[right]:
                left+=1
                right-=1
            else: 
                if self.judge(s[left+1:right+1]) or self.judge(s[left:right]):
                    return True
                else:
                    return False
        return True
    
    def judge(self,s):
        left=0
        right=len(s)-1
        while left<right:
            if s[left]==s[right]:
                left+=1
                right-=1
            else:
                return False
        return True
```
