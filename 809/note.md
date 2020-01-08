### 判断words里是否有string S 的简写
Let's see if a word is stretchy. Evidently, it needs to have the same key as S.  

Now, let's say we have individual counts c1 = S.count[i] and c2 = word.count[i].  

If c1 < c2, then we can't make the ith group of word equal to the ith word of S by adding characters.  

If c1 >= 3, then we can add letters to the ith group of word to match the ith group of S, as the latter is extended.  

Else, if c1 < 3, then we must have c2 == c1 for the ith groups of word and S to match.  

上面这段话是Solution给的思考。我们用一个itertools.groupby来遍历string，返回key和list, 注意前面要先将数据类型变为list。   例如heellhhoo得到key的就是(h,e,l,h,o),对应的len就是(1,2,2,2,2)。此处要注意与正常groupby的区别。  