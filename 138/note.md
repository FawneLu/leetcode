### hashtable
- 使用hashtable，在这个hash表里，记录了老链表和新链表的每一组对应。这样先构造了一个纯next的链表，然后再次循环就能得到带random的链表了。  
- 使用hashtable，直接存每个老节点对应的copy的节点。  如果该节点的next不在hashtable里，则加入, 然后cur.next = head.next  
如果该节点的random不在hashtable里，则加入, 然后cur.random = head.random  
然后head往后移，cur往后移。cur相当于在遍历copy的linkedlist