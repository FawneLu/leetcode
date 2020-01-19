### Sliding Window+Hashmap
right指针用来向后移动。  
hashmap用来存储字符串中的单词位子。 每次len(hashmap)>=distinct+1 时，就将hashmap中index最小的字母移去，  left=index+1。  
每次移动后都要更新max_len的长度。max_len=max(max_len, right-left)。