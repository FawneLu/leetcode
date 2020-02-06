### 动态规划
用两个数组hold和sell。  
hold表示该天手里有股票的最大收益， sell表示手里没有股票的最大收益。  
hold[i]=max(hold[i-1], (sell[i-2] if i>2 else 0)-prices[i])  
(第i天要么什么都不做，要么买入股票，买入股票的话证明前一天什么不做，且之前把股票卖了)  
sell[i]=max(hold[i-1]+prices[i], sell[i-1])  
(第i天要么把股票卖了，要么什么都不做)