```python
class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        n=len(nums)
        sums=[0]
        left=[0]*n
        right=[n-k]*n
        res=[0,0,0]
        mx=0
        for num in nums:
            sums.append(sums[-1]+num)
        
        total=sums[k]-sums[0]
        for i in range(k,n):
            if sums[i+1]-sums[i-k+1]>total:
                left[i]=i-k+1
                total=sums[i+1]-sums[i-k+1]
            else:
                left[i]=left[i-1]
        
        total=sums[n]-sums[n-k]
        for i in range(n-k-1,-1,-1):
            if sums[i+k]-sums[i]>=total:
                right[i]=i
                total=sums[i+k]-sums[i]
            else:
                right[i]=right[i+1]
                
        print(left)
        print(right)
                
        for i in range(k,n-2*k+1):
            l=left[i-1]
            r=right[i+k]
            total=sums[i+k]-sums[i]+sums[l+k]-sums[l]+sums[r+k]-sums[r]
            if total>mx:
                mx=total
                res=[l,i,r]
        
        return res
```