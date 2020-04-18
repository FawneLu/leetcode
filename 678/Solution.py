class Solution:
    def checkValidString(self, s: str) -> bool:
        visited=set([0])
        for c in s:
            new_s=set()
            if c=="(":
                for t in visited:
                    new_s.add(t+1)
            if c==")":
                for t in visited:
                    if t>0:
                        new_s.add(t-1)
            if c=="*":
                for t in visited:
                    new_s.add(t+1)
                    new_s.add(t)
                    if t>0:
                        new_s.add(t-1)
            visited=new_s
        
        return 0 in visited