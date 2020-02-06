### 快慢两个指针
利用在链表找是否有环的思路。  
这题也是设置快慢两个指针。slow=nums[slow], fast=nums[fast]  
slow=nums[slow]  
fast=nums[nums[fast]]  
他俩相遇时，fast再从零开始。  
slow=nums[slow]
fast=nums[fast]