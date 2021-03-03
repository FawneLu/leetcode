class Solution:
    def lastRemaining(self, n: int) -> int:
        if n<=1:
            return n
        return 2*(1+n//2-self.lastRemaining(n//2))

    def lastRemaining1(self, n: int) -> int:
    '''
    第一次从左向右检索完，剩下，2 4 6 8， 其实这跟1 2 3
4的信息几乎是一样的，只是差了倍数2，所以问题就变为从右往左对规模4的问题进行操作，找到答案乘以2就行。对于从右往左，如果是1 2 3 4
5的话，检索完还剩2 4，同样是1 2的问题，如果是 1 2 3 4，剩 1 3，我们可以认为是1
2乘以2减一，总之，我们可以找到将每次的剩余子序列转化为同类子问题的方法。
    '''
        def leftToright(n):
            if n == 1:
                return 1
            if n == 2:
                return 2
            
            if n%2 == 1:
                return 2*rightToleft((n-1)//2)
            else:
                return 2*rightToleft(n//2)
        
        
        def rightToleft(n):
            if n == 1:
                return 1
            if n == 2:
                return 1
            
            if n%2 == 1:
                return 2*leftToright((n-1)//2)
            else:
                return 2*leftToright(n//2) -1
        
        return leftToright(n)