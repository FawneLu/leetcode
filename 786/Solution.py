```python
class Solution:
    def kthSmallestPrimeFraction1(self, A: List[int], K: int) -> List[int]:
        h=[]
        for i in range(1,len(A)):
            heapq.heappush(h,(float(A[0]/A[i]),0,i))
        for x in range(K):
            v,p,q=heapq.heappop(h)
            if p+1<q:
                heapq.heappush(h,(float(A[p+1]/A[q]),p+1,q))
        return [A[p],A[q]]
    
    
    
    
    def kthSmallestPrimeFraction2(self, A: List[int], K: int) -> List[int]:
        ###超时了
        queue=[]
        for i in range(len(A)-1):
            for j in range(i+1,len(A)):
                if len(queue)<K:
                    heapq.heappush(queue,(-float(A[i]/A[j]),A[i],A[j]))
                else:
                    heapq.heappushpop(queue,(-float(A[i]/A[j]),A[i],A[j]))
        return [queue[0][1],queue[0][2]]
```
```
class Solution:
    def kthSmallestPrimeFraction(self, A: List[int], K: int) -> List[int]:
        nums = A
        k = K
        small = 0.0
        large = 1.0
        p = q = 0
        while large - small > 0.0000001:
            mid = small + (large-small)/2
            cnt = 0
            j = 0
            minDiff = 1.0
            for i in range(1,len(nums)):
                while j < i and nums[j]/nums[i] <= mid:
                    if minDiff > mid - nums[j]/nums[i]:
                        minDiff = mid - nums[j]/nums[i]
                        p = nums[i]
                        q = nums[j]
                    j+=1
                cnt += j
            if cnt == k:
                break;
            if cnt < k:
                small = mid
            else:
                large = mid 
        return (q,p)
```