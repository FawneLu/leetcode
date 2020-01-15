```python
"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""
class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        if not head:
            return None
        node=head
        while node:
            node_next=node.next
            if node.child:
                flattened=self.flatten(node.child)
                node.child=None
                nextnode=self.appendnode(node,flattened)
                node=nextnode
            else:
                node=node.next
        return head
    
    def appendnode(self,node,listtoappend):
        node_next=node.next
        node.next=listtoappend
        listtoappend.prev=node
        while node.next:
            node=node.next
        node.next=node_next
        if node_next:
            node_next.prev=node
        return node_next
```