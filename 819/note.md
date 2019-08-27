- 学会字典
这道题的思路其实很简单。先把string拆分成每个单词然后用字典存储每个单词的出现次数。然后再把不在banned里的出现次数最多的单词返回。
重点是要学会怎么用字典以及如何拆分string。
下面这句程序可以用来把str拆分成每个单词。
```python
re.split("\W+",str.lower())
```
可用内置函数Counter生成字典。
```python
from collections import Counter
count=Counter(list)
```
字典根据key排序
```python
dict=sorted(dict,key = dict.get, reverse = True)
```
