class Solution:
    def isNumber(self, s: str) -> bool:
        s = s.strip()
        isDigit, isDot, isE = False, False, False
        
        for i, c in enumerate(s):
            if c in "+-":
                if i != 0 and s[i-1] != "e":
                    return False
                
            elif c == "e":
                if not isDigit or isE:
                    return False
                isDigit = False
                isE = True
            
            elif c == ".":
                if isE or isDot:
                    return False
                isDot = True
            
            elif c.isdecimal():
                isDigit = True
            
            else:
                return False
        
        return len(s) > 0 and isDigit