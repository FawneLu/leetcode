### 二分查找
这道题的思路是用二分查最小化一个数组分成m个连续子数组的和的最大值。  
high是这个数组的和，low是sum/m，mid=low+(high-low)//2。判定条件是low < high。  
同时我们也要设一个flag来表示此时找的mid对不对。如果flag为true，表示可分，但此时mid还可以缩小， high=mid-1, 反之mid则找得太大了，不可分成m个。low=mid+1。  
循环中也应有个判定条件判断是否能分成m个连续子数组。 