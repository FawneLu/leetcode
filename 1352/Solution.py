class ProductOfNumbers:

    def __init__(self):
        self.prefix=[]
        self.index=0
        self.zero_index=-1
        
        

    def add(self, num: int) -> None:
        if num:
            if self.index:
                self.prefix.append(self.prefix[-1]*num)
            else:
                self.prefix.append(num)
        else:
            self.prefix.append(1)
            self.zero_index=self.index
        self.index+=1
        

    def getProduct(self, k: int) -> int:
        if self.zero_index>=self.index-k:
            return 0
        elif self.index==k:
            return self.prefix[-1]
        return self.prefix[-1]//self.prefix[self.index-k-1]