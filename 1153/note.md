### 字符串变化
这道题是看，一个字符串能否通过字母变化转化成另一个字符串。  
需要注意的是，如果其中一个字符串是26个字母，则肯定不存在。  
我们对str1进行enumerate，把对应的值和index对应的str2中的值存在字典里。