## 注意跟33题的区别
因为素=数组里包含重复的数字，所以每次求mid之前，要先移动左指针，确保左指针指向的数字与右指针不同。  
也因为有重复，所以要注意可以nums[mid] <= nums[right], nums[left] <= nums[mid]