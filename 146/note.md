### 自制一个LRU
tricky的地方是，只要访问了这个key，就从cache里把这个key移出然后放在LRU的最后。  
因为这个cache的容量只有2，这样做就可以保证最长时间没访问的key用在在第一个。