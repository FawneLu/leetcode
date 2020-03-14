class Solution:
    def nextGreaterElement(self, n: int) -> int:
        n=list(str(n))
        i=len(n)-1
        while i>0 and n[i-1]>=n[i]:
            i-=1
        if i==0:
            return -1
        self.reverse(n,i,len(n)-1)
        #print(n,i)
        for j in range(i,len(n)):
            if n[j]>n[i-1]:
                self.swap(n,j,i-1)
                break
        res = int("".join(n))
        return res if res<2**31 else -1
        
    
    def reverse(self,nums,i,j):
        for k in range(i,(i+j)//2+1):
            self.swap(nums,k,i+j-k)
        
    
    def swap(self,nums,i,j):
        nums[i],nums[j]=nums[j],nums[i]