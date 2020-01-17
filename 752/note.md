### yield
这道题要注意一个yield的使用。  
当你调用这个函数的时候，函数内部的代码并不立马执行 ，这个函数只是返回一个生成器对象，这有点蹊跷不是吗。

那么，函数内的代码什么时候执行呢？当你使用for进行迭代的时候.

现在到了关键点了！

第一次迭代中你的函数会执行，从开始到达 yield 关键字，然后返回 yield 后的值作为第一次迭代的返回值. 然后，每次执行这个函数都会继续执行你在函数内部定义的那个循环的下一次，再返回那个值，直到没有可以返回的。

如果生成器内部没有定义 yield 关键字，那么这个生成器被认为成空的。这种情况可能因为是循环进行没了，或者是没有满足 if/else 条件。  
我们用一个函数来求一个node可以到达的所有情况。 
```python 
def neighbours(node):
            for i in range(4):
                x=int(node[i])
                for d in (-1,1):
                    y=(x+d)%10
                    yield node[:i]+str(y)+node[i+1:]```python
```  
这里也要注意负数取余的操作 n%10=n-10* (n//10),n<0, ‘//’ 表示向下取余。  
把（node,depth） append 到一个queue里。 每次取出。 如果node在deadends里则continue。 对在node的 neirghbours的nodes里进行循环，如果 n被查过了则添加到seen里，否则把（n, depth+1） append 到queue里。