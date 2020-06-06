### 类似找规律的题
对于每个最高位来说，他有(n-1)!中排列组合。由此，我们可以依次确定每一位。
用一个数组存放对于每一位来说的排列组合的个数。  
Generate input array nums of numbers from 1 to N .    

Compute all factorial bases from 0 to (N - 1)!.  

Decrease kk by 1 to make it fit into (0, N! - 1) interval.  

Compute factorial representation of kk. Use factorial coefficients to construct the permutation.  

Return the permutation string.  