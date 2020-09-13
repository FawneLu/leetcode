## 排序
数组排序。这里用了快排和mergesort
快排注意了，假设right为pivot, 相当于用两个指针，i，j，分别从left和right-1的地方出发。  
i的左边不包括i，全都小于pivot, j的右边不包括j全都大于等于pivot。  
如果nums[i] >= pivot, swap(nums[i], pivot), then j--