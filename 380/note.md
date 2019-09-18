- 空间复杂度低
1. 用table存储数和它对应的位置，list存储数。  
2. 交换list中要删除的数和list的最后一个数，然后pop，同时删掉table中的数。  
3. 用random.randint（）选择。

- 直接用set
最后选择的时候将set变为list.