### 不知道这算是啥题
首先对words按长度进行排序。  然后用一个函数来判断两个长度不同的words是否能用长的words去掉一个字母后相等。  
```python
def check(str1,str2):
            tmp=""
            for i in range(len(str2)):
                tmp=str2[:i]+str2[i+1:]
                if tmp==str1:
                    return True
            return False
```  
然后再进行循环判断。  
