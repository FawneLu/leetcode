### Flatten a linkedlist
把一个带child的节点展开变成一个linkedlist。  
现在的思路就是每次遇到child节点，就把这个节点作为当前node的next节点；并且要遍历child节点后面的所有节点，找到child链表最后面的节点，作为要插入的一整段链表最后的节点，即原node.next节点prev节点。

做法需要新定义一个函数，这个函数对每个child链表进行遍历，把整段的child链表插入到原链表中。  
DFS负责查找，新定义的函数负责插入。
