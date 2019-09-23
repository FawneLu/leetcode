```python
class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        table = {char:code for char,code in zip("abcdefghijklmnopqrstuvwxyz",[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."])}
        print(table)
        trans = set()
        for word in words:
            trans.add("".join([table[char] for char in word]))
            
        return len(trans)
```