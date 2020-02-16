```python
class Solution:
    def toGoatLatin(self, S: str) -> str:
        vowel=('a','e','i','o','u','A','E','I','O','U')
        new_str=S.split(' ')
        res=""
        for i,word in enumerate(new_str):
            if word[0] in vowel:
                word+='ma'
            else:
                word=word[1:]+word[0]+'ma'
            
            word+='a'*(i+1)
            res+=(word+' ')
            
        return res[:-1]
```