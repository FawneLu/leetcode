class Trie:
    # word_end = -1
 
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = {}
        self.word_end = -1
 
    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        curNode = self.root
        for c in word:
            if not c in curNode:
                curNode[c] = {}
            curNode = curNode[c]
          
        curNode[self.word_end] = True
 
    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        curNode = self.root
        for c in word:
            if not c in curNode:
                return False
            curNode = curNode[c]
            
        # Doesn't end here
        if self.word_end not in curNode:
            return False
        
        return True
 
    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        curNode = self.root
        for c in prefix:
            if not c in curNode:
                return False
            curNode = curNode[c]
        
        return True

————————————————
版权声明：本文为CSDN博主「凌疯墨子」的原创文章，遵循 CC 4.0 BY-SA 版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/ANNILingMo/article/details/80879910