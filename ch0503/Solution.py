class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(magazine)<len(ransomNote):
            return False
        
        if not ransomNote:
            return True
        
        
      
        for r in ransomNote:
            i=0
            while i<len(magazine):
                if r==magazine[i]:
                    new_magazine=magazine[:i]+magazine[i+1:]
                    break
                else:
                    i+=1
            if i==len(magazine):
                return False
            magazine=new_magazine

        
        return True