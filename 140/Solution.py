```python
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        visited=dict()
        return self.dfs(s,[],visited,wordDict)
    
    def dfs(self,s,res,visited,wordDict):
        if s in visited:
            return visited[s]
        
        if not s:
            return ['']
        
        res=[]
        for word in wordDict:
            if s[:len(word)]!= word:continue
            for r in self.dfs(s[len(word):],res,visited,wordDict):
                res.append (word+("" if not r else " "+r))
                
        visited[s]=res
        
        return res
```