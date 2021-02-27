class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        res = set()
        hashmap = collections.defaultdict(list)
        for t in transactions:
            t = t.split(",")
            hashmap[t[0]].append(t)
        #print(hashmap)
        
        for key in hashmap:
            t = hashmap[key]
            for i in range(len(t)):
                for j in range(i):
                    if t[i][3] != t[j][3] and int(t[i][1])-int(t[j][1])<60:
                        res.add(",".join(t[i]))
                        res.add(",".join(t[j]))
                if int(t[i][2]) > 1000:
                    res.add(",".join(t[i]))
        
        return res