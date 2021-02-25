class ListNode:
    def __init__(self,x):
        self.val = x
        self.prev = None
        self.next = None
        
class BrowserHistory1:

    def __init__(self, homepage: str):
        self.root = ListNode(homepage)
        

    def visit(self, url: str) -> None:
        node = ListNode(url)
        self.root.next = node
        node.prev = self.root
        self.root = self.root.next
        
        

    def back(self, steps: int) -> str:
        while steps and self.root.prev:
            self.root = self.root.prev
            steps -= 1
        
        return self.root.val
        

    def forward(self, steps: int) -> str:
        while steps and self.root.next:
            self.root = self.root.next
            steps -= 1
        
        return self.root.val


class BrowserHistory:

    def __init__(self, homepage: str):
        self.history = [homepage]
        self.future = []

        

    def visit(self, url: str) -> None:
        self.history.append(url)
        self.future = []
        
        
        

    def back(self, steps: int) -> str:
        while steps and len(self.history) > 1:
            self.future.append(self.history.pop())
            steps -= 1
        return self.history[-1]
        
        

    def forward(self, steps: int) -> str:
        while steps and len(self.future):
            self.history.append(self.future.pop())
            steps -= 1
        return self.history[-1]