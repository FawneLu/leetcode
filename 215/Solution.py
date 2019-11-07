```python3
import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap=[]
        
        for num in nums:
            heapq.heappush(heap, num)
            if len(heap)>k:
                heapq.heappop(heap)
                
        return heapq.heappop(heap)
```
```python3
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
    	
        def buildHeap(nums,length):
            i=int(length/2)
            while i>=1:
                heapify(nums,length,i)
                i-=1
            return nums
        
        def heapify(nums,length,i):
            while True:
                maxPos=i
                if(i*2<=length and nums[i]<nums[i*2]):
                    maxPos=i*2
                if(i*2+1<=length and nums[maxPos]<nums[i*2+1]):
                    maxPos=i*2+1
                if maxPos==i:
                    break
                nums[i],nums[maxPos]=nums[maxPos],nums[i]
                i=maxPos
               
        nums_=[]
        nums_.append(None)
        for num in nums:
            nums_.append(num)
        length=len(nums)
        buildHeap(nums_,length)
        i=length
        while i>1:
            nums_[1],nums_[i]=nums_[i],nums_[1]
            i-=1
            heapify(nums_,i,1)
        return nums_[-k]
            
```