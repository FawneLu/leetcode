### 设计一个hashtable
首先，hash怎么算。在这边我们用取余的方法  
其次，解决哈希冲突，一共三种办法：  
1. 开放寻址 
a. 线性探测， 每次加1  
b. 二次再探测， 左右来回探测  
c. 伪随机探测   
2. 链接法  
3. 再次哈希： 构造多个哈希函数。    
Overall, there are several strategy to resolve the collisions:    

Separate Chaining: for values with the same hash key, we keep them in a bucket, and each bucket is independent from each other.  

Open Addressing: whenever there is a collision, we keep on probing on the main space with certain strategy until a free slot is found.  

2-Choice Hashing: we use two hash functions rather than one, and we pick the generated address with fewer collision.  

Solution用了开放寻址方式和separate chaining