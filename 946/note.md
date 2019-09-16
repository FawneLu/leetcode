- 我想不出来
For this question, we need to come up with one thing that whether the element in the stack is the same with the popped's top element.  
1. We append pushed's first element in the stack. 
2. If the top element in the stack is the same with fisrt element in the popped, then we pop stack and stack.  
For lower time complexity, we need to reverse pushed and popped. We also use pushed==[] to as the termination maker.

这道题，我们每次都判断stack的最后一个元素是否跟popped的第一个元素相等。如果相等，两个同时出栈。如果不等，我们把pushed元素按顺序压入栈中。
为了减少时间复杂度，我们可以先反转pushed和popped两个list。