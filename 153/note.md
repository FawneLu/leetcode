### binary search找数组里最小的数
思路就是二分查找  
有mid之后判断：  
1. nums[mid+1]< nums[mid]:return nums[mid+1]  
2. nums[mid-1]>nums[mid]:return nums[mid]  
3. 如果 nums[mid]>nums[0]，说明left小了， 要往右找， 否则往左找。