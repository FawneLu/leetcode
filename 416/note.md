### dp
用一个二维矩阵存储前i个数有没有构成和为j的可能。  
j的取值范围是0~sum。  
我们最后返回dp[len(nums)][sum/2]