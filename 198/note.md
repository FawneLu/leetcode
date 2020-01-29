### 这道题很有意思
- 首先可以用dp, 边界条件是：  
dp[0]=nums[0]
dp[1]=max(nums[1],nums[0])  

- 用一个prev, 一个cur  
temp = prev # This represents the nums[i-2]th value  
prev = cur # This represents the nums[i-1]th value   
cur=max(num+temp,prev)

