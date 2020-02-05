```python
class Node(object):
    def __init__(self):
        self.children = collections.defaultdict(Node)
        self.isword = False
        
class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root=Node()
        

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        current=self.root
        for s in word:
            current=current.children[s]
        current.isword=True
        

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        current=self.root
        for s in word:
            current=current.children.get(s,None)
            if current==None:
                return False
        
        return True if current.isword else False
            

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        current=self.root
        for s in prefix:
            current=current.children.get(s,None)
            if current==None:
                return False
        
        return True
        
        
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
```