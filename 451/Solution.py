class Solution:
    def frequencySort1(self, s: str) -> str:
        s_count = collections.Counter(s)
        res = []
        for letter,freq in s_count.most_common():
            res.append(letter*freq)
        
        return "".join(res)
    
    def frequencySort(self, s: str) -> str:
        if not s: return s
        s_count = collections.Counter(s)
        max_freq = max(s_count.values())
        
        buckets = [[] for _ in range(max_freq+1)]
        for c, i in s_count.items():
            buckets[i].append(c)
        
        res = []
        for i in range(len(buckets) -1, 0 ,-1):
            for c in buckets[i]:
                res.append(c*i)
        
        return "".join(res)