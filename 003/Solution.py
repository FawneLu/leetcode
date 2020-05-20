```python3
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # if s=="":
        #     return 0
        # sub=""
        # max_len=1
        # j=0
        # while j<=len(s)-1:
        #     sub=""
        #     i=j
        #     while i<=len(s)-1:
        #         if s[i] not in sub:
        #             sub=sub+s[i]
        #             i+=1
        #         else:
        #             sub=""
        #         max_len=max(max_len,len(sub))
        #     j+=1
        # return max_len
        max_len=1
        if not s:
            return 0
        sub=set(s[0])
        i=0
        for j in range(1,len(s)):
            if s[j] not in sub:
                sub.add(s[j])
            else:
                while s[i]!=s[j]:
                    sub.remove(s[i])
                    i+=1
                i+=1
            max_len=max(max_len,len(sub))
        return max_len

        def lengthOfLongestSubstring(self, s: str) -> int:
        left,right=0,0
        res=0
        visited=set()
        for left in range(len(s)):
            while right<len(s) and s[right] not in visited:
                visited.add(s[right])
                res=max(res,right-left+1)
                right+=1
            visited.remove(s[left])
        
        return res
        
```
