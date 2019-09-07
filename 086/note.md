- LinkedList太难了
这道题，换种思路其实很简单。我们用一个small的链表存储比x小的数，用一个large的链表存储大于等于x的数。small_r和large_r分别指向两个两个链表。遍历完链表之后把两个链表拼接起来就可以了。
我们可以注意的地方是，如果循环条件是while head,此时直接用head=head.next的话当遍历到链表的最后一位会有问题，此时我们可以设一个tmp。tmp=head.next, head.next=None, head=tmp。
