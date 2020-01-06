- dfs
这道题用了深度优先遍历的思想。  
先把pairs存在字典里，再对words1.words2进行深度优先遍历，直到在words2中找出words1的近义词，否则则返回false。