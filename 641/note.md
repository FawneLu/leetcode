- 跟单项循环队列同样的思路
我们需要记住对单项队列来说队空就是tail==head，队满就是tail==n，tail总指向当前空位置。  
对于循环队列来说，队空同样是tail==head。队满时，如果同样tail==head就不好判断，所以实际情况中我们多留一个空位置。判断就是(tail+1)%k==head。