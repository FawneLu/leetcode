超时，运行不了  
```python
class StreamChecker:

    def __init__(self, words: List[str]):
        self.words=set(words)
        self.pre=''

    def query(self, letter: str) -> bool:
        self.pre+=letter
        for i in range(len(self.pre)):
            if self.pre[-i-1:] in self.words:
                return True
        return False


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
```  
用Trie Tree  
```python
class StreamChecker:
    def __init__(self, words: List[str]):
        self.Trie={}
        self.pre=''
        for word in words:
            curnode=self.Trie
            word=word[::-1]
            for ch in word:
                if ch not in curnode:
                    curnode[ch]={}
                curnode=curnode[ch]
            curnode['#']=1
        

    def query(self, letter: str) -> bool:
        self.pre+=letter
        curnode=self.Trie
        for i in range(len(self.pre)):
            if self.pre[-i-1] not in curnode :
                break
            curnode=curnode[self.pre[-i-1]]
            if '#' in curnode:
                return True
        return False
```