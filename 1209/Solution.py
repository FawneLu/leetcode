class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        if not s or len(s) == 1:
            return s
        
        i = 0
        stack = []
        
        while i < len(s):
            c = s[i]
            if stack and s[i] == stack[-1][0]:
                while i < len(s) and s[i] == c:
                    stack[-1][1] += 1
                    i += 1
                
                
                while stack[-1][1] - k >= 0:
                    stack[-1][1] -= k  
                if stack[-1][1] == 0:
                    stack.pop()
                    
                
            else:
                stack.append([s[i], 1])
                i += 1
     
        res = ""
        for i in stack:
            for j in range(i[1]):
                res += i[0]
                
        return res