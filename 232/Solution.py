```python
class MyQueue(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack=[]
        

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: None
        """
        self.stack.append(x)
        

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        #first_pop=self.stack.pop(0)
        
        if not self.stack:
            return None
        
        tmp=[]
        while self.stack:
            tmp.append(self.stack.pop())
            
        top=tmp.pop()
        
        while tmp:
            self.stack.append(tmp.pop())
        
        return top
    
    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        #return self.stack[0]
        
        
        
        tmp=[]
        while self.stack:
            tmp.append(self.stack.pop())
        
        top=tmp[-1]
        
        while tmp:
            self.stack.append(tmp.pop())
        
        return top
        

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        if self.stack==[]:
            return True
        else:
            return False


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
```