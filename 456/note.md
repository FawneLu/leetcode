### stack
这道题的思路很巧妙，用一个stack存储数。从后往前遍历数组如果num>stack[-1]则把stack[-1] pop出来，j=stack[-1], stack里的数一定是单调递减。  
j用来表示比当前num小的最大的数。如果后面有num< j, 则符合条件， return True。