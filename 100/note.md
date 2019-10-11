- 这道题算是自己写出来的吧...
首先一个我们要注意的问题是python中‘==’比较的是两个对象的地址。python2中可以直接用_cmp_function进行比较。python3删除了这个函数，所以我们需要分开比较。  
这道题开始判断if not p or not q,我们需要判断的是两个树是不是为空。如果有空，就不存在有id的问题。但是两个树都为空的话，我们也只需要返回true。所以判断结果为返回怕p==q.  
如果分开写的话就是if p and not q, if not p and q, if not p and not q.分别返回false，false，true。