```python
class Solution:
    def isNStraightHand(self, hand: List[int], W: int) -> bool:
        cards=collections.Counter(hand)
        while cards:
            start_index=min(cards.keys())
            start_val=cards[start_index]
            for i in range(start_index,start_index+W):
                if i not in cards:
                    return False
                cards[i]-=start_val
                if cards[i]==0:
                    cards.pop(i)
                if cards[i]<0:
                    return False
        
        return not cards
```