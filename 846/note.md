### 暴力解法
把hand变为一个dict，查看每个牌有多少张。要想组成连续的数串，后一张牌的个数必须大于等于前一张牌的个数。  
每一次循环开始都是dict里最小的牌，循环W次。