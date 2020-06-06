class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        res=""
        num=[str(i) for i in range(1,10)]
        loop=[1]*n
        for i in range(1,n):
            loop[i]=loop[i-1]*i
        
        k-=1
        for i in range(n,0,-1):
            cur_ind=k//loop[i-1]
            res+=num[cur_ind]
            k%=loop[i-1]
            num.pop(cur_ind)
        return res