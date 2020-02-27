```python
class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        stack=[float('inf')]
        res=0
        for num in arr:
            while stack[-1]<=num:
                mid=stack.pop()
                res+=mid*min(stack[-1],num)
            stack.append(num)
        while len(stack)>2:
            res+=stack.pop()*stack[-1]
        return res
    
    def mctFromLeafValues1(self, arr: List[int]) -> int:
        if not arr:
            return 0
        visited={}
        def helper(i,j):
            if i>=j:
                return 0
            if (i,j) in visited:
                return visited[(i,j)]
            res=float('inf')
            for k in range(i+1,j+1):
                res=min(res,helper(i,k-1)+helper(k,j)+max(arr[i:k])*max(arr[k:j+1]))
                visited[(i,j)]=res
            return res
        
        return helper(0,len(arr)-1)
```