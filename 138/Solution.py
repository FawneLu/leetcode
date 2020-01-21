```python
"""
# Definition for a Node.
class Node:
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random
"""
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        nodedict=dict()
        dummy=Node(0,None,None)
        nodedict[head]=dummy
        newhead=dummy
        pointer=head
        
        while pointer:
            node=Node(pointer.val, pointer.next, None)
            nodedict[pointer]=node
            newhead.next=node
            newhead=newhead.next
            pointer=pointer.next
        
        pointer=head
        while pointer:
            if pointer.random:
                nodedict[pointer].random=nodedict[pointer.random]
            pointer=pointer.next
        
        return dummy.next
```