- 思路正确，写法有问题
这道题的思路是，我们把要删掉的节点的前一个节点的指针指向要删掉的节点的后一个节点。我们可以用count来找，也可以用两个指针一个quick，一个slow（这是张老师的思路）。用quick和slow就是quick永远比slow快n。所以当quick指向空时，slow正好指向被删除节点的前一个节点。