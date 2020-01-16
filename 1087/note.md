### Recursion
这道题的思路是，我们用一个函数来进行recursion。  
return的条件是字符串为空。  用一个tmp来记录结果。如果当前是字母，则把它加到tmp上，如果不是，我们找出'}' 对应的index，我们需要递归操作的字符串substring就是s[1:i]，然后再对substring进行操作，substring.split(',')， 然后对中间的字母进行排序后，循环递归。