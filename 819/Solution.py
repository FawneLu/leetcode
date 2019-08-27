```python3
from collections import Counter
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        
        list1=re.split("\W+",paragraph.lower())
        count=Counter(list1)
        print (count)
        
#         set1=set(list1)
        
#         list2=list(set1)
#         count={}
#         for x in range(len(list2)): 
#             count[list2[x]] = 0  
#             for y in range(len(list1)):
#                 if list2[x] == list1[y]:
#                     count[list2[x]] += 1

        
        count=sorted(count,key = count.get, reverse = True)
        
        print (count)
        
        banned=set(banned)
        for word in count:
            if word and word not in banned:
                return word
        return ""
```
