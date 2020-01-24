### 最大顶堆和最小顶堆
1. 大顶堆中存储的元素均不大于小顶堆中的元素  
2. MaxHeap.size() == MinHeap.size()，或者 MaxHeap.size() == MinHeap.size() + 1  

当MaxHeap.size() == MinHeap.size() + 1时，中位数就是MaxHeap的堆顶元素  

当MaxHeap.size() == MinHeap.size()时，中位数就是MaxHeap堆顶元素与MinHeap堆顶元素的均值