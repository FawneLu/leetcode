### 二分查找
我们用binary search来查找一个list里放置一个数x的index，使得，list[:i]< x, list[i+1:]>x, 这个位置就是我们每次求得的结果。

###用mergesort的思路
这个方法真的是fucking genius。  
enumerate数组之后，不断二分，然后把enumerate的左右的数组进行排序。 不断把右边往左边插，看右边的前面的enum插了几个就证明了有几个数在后面比它小