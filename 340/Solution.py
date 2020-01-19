```python
class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        n=len(s)
        if k==0 or n==0:
            return 0
        
        left,right=0,0
        hashmap=collections.defaultdict()
        max_len=1
        
        while right<n:
            hashmap[s[right]]=right
            right+=1
            
            if len(hashmap)>=k+1:
                index=min(hashmap.values())
                del hashmap[s[index]]
                left=index+1
                
            max_len=max(max_len,right-left)
        
        return max_len
```