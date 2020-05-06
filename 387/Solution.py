class Solution:
    def firstUniqChar(self, s: str) -> int:
        count=collections.Counter(s)
        for i in count:
            if count[i]==1:
                return s.index(i)
        return -1