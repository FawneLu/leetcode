### BFS
 layer = {}，这个东西是一个dictionary， layer[word] = [ path1, path2 , path3 , ... ] ，其中每一个path都是以word结束的一组单词list，代表路径。
wordList -= set(newlayer.keys()) 是保证 BFS。