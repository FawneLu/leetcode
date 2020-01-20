### 这算是什么类型的题呢
先求出每个坐标i 左边最高的bar和右边最高的bar。  
res+=min(max_left[i], max_right[i])-height[i]