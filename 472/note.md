### word break进阶版
想道题比word break多的地方是所有词都在一个list里，判断每个词能否由剩余的单词组成。  
每次只需把判断的词移出，当做一个单独的word，再用word break的方法就可以了。  
需要注意，每次判断完还需将word放回list。