- 栈实现队列
一般的思路是我们用两个栈实现队列。先把数全都压进一个栈里，然后弹出到另一个栈。注意，我们也需要再恢复原来的栈方便后续操作。
但是在python里，我们可以用pop(0)，这样的做法会增大时间复杂度。deque也是一种投机取巧的方式，但是与pop(0)不同，它的时间复杂度更低。