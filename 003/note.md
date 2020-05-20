### 窗口滑动指针问题
- 这题好难
哈哈哈哈哈，每一个string我都觉得好难。还是我太菜了。这题按照自己的思路就是，从第一个单词开始遍历，遇到重复的就跳出，再从第二个开始。这个思路也是可以的，除了浪费时间，所以还真的超时了。
按照张老师的思路就是，我们设两个poniter，一个指向当前元素，一个用来遍历元素，如果这个元素在sub里，就把i和j之间的元素删掉，i再加1，相当于从重复元素的后一位再开始遍历。
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
        
```

