```python
class TrieNode:
    def __init__(self):
        self.children = dict()
        self.isWord = False
class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word):
        node = self.root
        for letter in word:
            child = node.children.get(letter)
            if child is None:
                child = TrieNode()
                node.children[letter] = child
            node = child
        node.isWord = True
        
    def search(self, word):
        node = self.root
        for letter in word:
            node = node.children.get(letter)
            if node is None:
                return False
        return node.isWord
    
    def startsWith(self, prefix):
        node = self.root
        for letter in prefix:
            node = node.children.get(letter)
            if node is None:
                return False
        return True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        m = len(board)
        n = len(board[0])
        trie = Trie()
        for w in words:
            trie.insert(w)
        ans = []
        for i in range(m):
            for j in range(n):
                tmp = [[0 for q in range(n)] for q in range(m)]
                str = board[i][j]
                self.dfs(i,j,trie,board,tmp,str,ans)   
        return ans
    
    def dfs(self,i,j,trie,board,tmp,str,ans):
        m = len(board)
        n = len(board[0])
        tmp[i][j] = 1
        if trie.startsWith(str) == False:
            tmp[i][j] = 0
            return
        if trie.search(str) and str not in ans:
            ans.append(str)
        
        dz=zip((0,0,-1,1),(-1,1,0,0))
        for dx,dy in dz:
            nx=dx+i
            ny=dy+j
            if nx>=0 and ny>=0 and nx<m and ny<n and not tmp[nx][ny] :
                self.dfs(nx,ny,trie,board,tmp,str+board[nx][ny],ans)
        tmp[i][j] = 0
```