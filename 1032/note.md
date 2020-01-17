### 用前缀树解决  
把words里的每个word按倒叙放在树里。  
查找的时候也从最后一位开始往前查找。没有就break，有的话curnode=curnode[当前的字母]