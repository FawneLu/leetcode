class Solution:
    def isAnagram1(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        count = [0] * 26
        for i in range(len(s)):
            count[ord(s[i]) - ord('a')] += 1
            count[ord(t[i]) - ord('a')] -= 1
        
        for num in count:
            if num != 0:
                return False
        
        return True
    
    
    def isAnagram2(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s.sort()
        t.sort()
        if s != t :
            return False
        return True
    
    
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        count_s = collections.Counter(s)
        count_t = collections.Counter(t)
        for idx in count_t:
            if idx not in count_t or count_t[idx] != count_s[idx]:
                return False
        return True