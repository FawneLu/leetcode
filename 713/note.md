## 滑动窗口
这道题的思路也是用一个滑动窗口来做。  
当乘积大于等于k时，就不断地开始除前面的数。  
巧妙的地方是，每增加一个数，结果就增加 j-i+1， 可推导