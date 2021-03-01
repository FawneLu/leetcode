from heapq import *
class Leaderboard:

    def __init__(self):
        self.dict = collections.defaultdict(int)
        

    def addScore(self, playerId: int, score: int) -> None:
        self.dict[playerId] += score
        

    def top(self, K: int) -> int:
        self.l  = []
        heapify(self.l)
        for pid, score in self.dict.items():
            if len(self.l) >= K:
                if score > self.l[0]:
                    heappush(self.l,score)
                    heappop(self.l)
            else:
                heappush(self.l,score)
        
        return sum(self.l)
        

    def reset(self, playerId: int) -> None:
        self.dict[playerId] = 0
        


# Your Leaderboard object will be instantiated and called as such:
# obj = Leaderboard()
# obj.addScore(playerId,score)
# param_2 = obj.top(K)
# obj.reset(playerId)