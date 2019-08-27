- String好难，我枯了（枯得太早
For this problem, we use a pointer to determing whether the current number is the same with previous one. If yes then we set count+=1. If no, then we store the letter and its number(we use str(count)). What we need to pay attention to is that, after the loop, we need to store the last letter and its number.
```python
class Solution:
    def compress(self, chars: List[str]) -> int:
        pre=chars[0]
        count=0
        index=0
        for char in chars:
            if char==pre:
                count+=1
            else:
                chars[index]=pre
                index+=1
                if count>1:
                    for num in str(count):
                        chars[index]=num
                        index+=1
                pre=char
                count=1
        
        chars[index]=char
        index+=1
        if count>1:
            for num in str(count):
                chars[index]=num
                index+=1
                
        print (chars)
        
        return index
```
