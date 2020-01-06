```python
class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls = 0
        cows = 0
        secret_dict = collections.defaultdict(int)
        for s, g in zip(secret, guess):
            if s == g:
                bulls += 1
            else:
                secret_dict[s] += 1
        for i, g in enumerate(guess):
            if secret[i] != guess[i] and secret_dict[g]:
                cows += 1
                secret_dict[g] -= 1
        return str(bulls) + "A" + str(cows) + "B"
```