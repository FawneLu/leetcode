```python
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        phone = {'2': ['a', 'b', 'c'],'3': ['d', 'e', 'f'],'4': ['g', 'h', 'i'],'5': ['j', 'k', 'l'],'6': ['m', 'n', 'o'],'7': ['p', 'q', 'r', 's'],'8': ['t', 'u', 'v'],'9': ['w', 'x', 'y', 'z']}

        def helper(combination, digits):
            
            if len(digits)==0:
                res.append(combination)
            else:
                for letter in phone[digits[0]]:
                    helper(combination+letter,digits[1:])
        
        res=[]
        if digits:
            helper("",digits)
        return res
```