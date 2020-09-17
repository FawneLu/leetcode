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
        if not head:
            return None
        
        lookup = dict()
        newhead = Node(head.val, None, None)
        lookup[head] = newhead
        cur = newhead
        
        while head:
            if head.next:
                if head.next not in lookup:
                    lookup[head.next] = Node(head.next.val, None, None)
                
                cur.next = lookup[head.next]
            
            if head.random:
                if head.random not in lookup:
                    lookup[head.random] = Node(head.random.val, None, None)
                
                cur.random = lookup[head.random]
            
            head = head.next
            cur = cur.next
        
        return newhead
        
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
