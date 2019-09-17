```python
class MyCircularDeque:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the deque to be k.
        """
        self.k=k+1
        self.items=[-1]*self.k
        self.tail=self.head=0

    def insertFront(self, value: int) -> bool:
        """
        Adds an item at the front of Deque. Return true if the operation is successful.
        """
        if self.isFull():
            return False
        else:
        
            self.head=(self.head+self.k-1)%self.k
            self.items[self.head]=value

            return True
        

    def insertLast(self, value: int) -> bool:
        """
        Adds an item at the rear of Deque. Return true if the operation is successful.
        """
        if self.isFull():
            return False
        
        else:
        
            self.items[self.tail]=value
            self.tail=(self.tail+1)%self.k

            return True

    def deleteFront(self) -> bool:
        """
        Deletes an item from the front of Deque. Return true if the operation is successful.
        """
        if self.isEmpty():
            return False
        
        else:
        
            self.items[self.head]=-1
            self.head=(self.head+1)%self.k

            return True
        

    def deleteLast(self) -> bool:
        """
        Deletes an item from the rear of Deque. Return true if the operation is successful.
        """
        if self.isEmpty():
            return False
        
        else:
        
            self.tail=(self.tail+self.k-1)%self.k
            self.items[self.tail]=-1

            return True
        

    def getFront(self) -> int:
        """
        Get the front item from the deque.
        """
        if self.isEmpty():
            return -1
        
        else:
            value=self.items[self.head]
            return value
        

    def getRear(self) -> int:
        """
        Get the last item from the deque.
        """
        if self.isEmpty():
            return -1
        
        else:
            index=(self.tail+self.k-1)%self.k
            return self.items[index]
        

    def isEmpty(self) -> bool:
        """
        Checks whether the circular deque is empty or not.
        """
        return True if self.head==self.tail else False
        

    def isFull(self) -> bool:
        """
        Checks whether the circular deque is full or not.
        """
        return True if (self.tail+1)%self.k==self.head else  False


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()
```