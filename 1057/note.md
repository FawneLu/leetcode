### 这道题不难但是好复杂哦
这道题的意思是输出一个list是自行车的编号，对应的人的编号是[0,1,...,n]，是的对应的距离最短，如果两者对应的距离相同我们就选择worker编号小的那一个。  
然后用每次按顺序把每个worker的最小距离和对应的bike取出来，存入used_bike里。  
如果bike已经在used_bike里，则取对应的worker第二小的距离和自行车。