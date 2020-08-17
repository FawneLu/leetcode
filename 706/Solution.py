#开放寻址法
class HashTable:

    # 初始化
    def __init__(self, size):
        self.bucket = [None for _ in range(size)]                # 创建一个列表保存哈希元素,值全为None
        self.count = size                                      # 最大表长

    # 散列函数
    def hash(self, key):
        return key % self.count                                # 散列函数采用除留余数法

    # 插入
    def insert_hash(self, key):
        address = self.hash(key)                               # 计算散列地址
        while self.bucket[address] != None:                      # 发生冲突
            address = (address + 1) % self.count               # 线性探测解决冲突
        self.bucket[address] = key                               # 没有冲突

    # 查找
    def search_hash(self, key):
        # star = address = self.hash(key)                               # 查找关键字
        # while self.bucket[address] != key:
        #     address = (address + 1) % self.count
        #     if not self.bucket[address] or address == star:             # 说明没找到或者循环到了开始的位置
        #         return False
        # return True
        
        for (k,v) in self.bucket:
            if k == key:
                return val
        return -1


    #删除
    def remove_hash(self, key):
        address = self.hash(key)
        for i, kv in enumerate(self.bucket):
            if kv[0] == key:
                del self.bucket[i] 


#拉链法解决hash collision
class ListNode(object):
    def __init__(self,key):
        self.key = key
        self.val = None
        self.next = None

class MyHashMap:
    SIZE = 1000
    
    def __init__(self):
        self.hashing = [ListNode(-1) for _ in range(self.SIZE)]
    
    def put(self, key, value):
        head = self.hashing(key % self.SIZE)
        current = head.next
        while current:
            if current.key == key:
                break
            current = current.next
        
        else:
            current = ListNode(key)
            current.next = head.next
            head.next = current
        
        current.val = value
    
    def get(self, key):
        current = self.hashing(key % self.SIZE)
        while current :
            if current.key == key:
                break
            current = current.next
        
        else:
            return -1
        
        return current.val
    
    def remove(self, key):
        current = self.hashing(key % self.SIZE)
        while current and current.next:
            if current.next.key = =key:
                break
            current = current.next
        
        else:
            return None
        
        current.next = current.next.next
            
        
        
        
# 数组代替链表
class Bucket:
    def __init__(self):
        self.bucket=[]
        
    def get(self,key):
        for (k,v) in self.bucket:
            if k == key:
                return v

        return -1
        
    def update(self,key,value):
        found = False
        for i,kv in enumerate(self.bucket):
            if kv[0] == key:
                self.bucket[i] = (key,value)
                found = True
                break
            
        if not found:
            self.bucket.append((key,value))
                
    def remove(self,key):
        for i,kv in enumerate(self.bucket):
            if kv[0] == key:
                del self.bucket[i]

# for Bucket
class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.key_space = 2069
        self.hash_table = [Bucket() for i in range(self.key_space)]
        

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        hash_key = key % self.key_space
        self.hash_table[hash_key].update(key,value)

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        hash_key = key % self.key_space
        return self.hash_table[hash_key].get(key)

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        hash_key = key % self.key_space
        self.hash_table[hash_key].remove(key)