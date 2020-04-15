class Solution:
    def canTransform(self, start: str, end: str) -> bool:
        if len(start)!=len(end):
            return False
        
        A=[(i,s) for i,s in enumerate(start) if s=="L" or s=="R"]
        B=[(ind,e) for ind,e in enumerate(end) if e=="L" or e=="R"]
        
        if len(A)!=len(B):
            return False
        
        for (a,s),(b,e) in zip(A,B):
            if s!=e:
                return False
            if s=="L" and a<b:
                return False
            if s=="R" and a>b:
                return False
        
        return True