class Solution:
    def findMinStep(self, board: str, hand: str) -> int:
        def remove(b):
            i = 0
            for j in range(len(b)+1):
                if j == len(b) or b[j] != b[i]:
                    if j - i >= 3:
                        return remove(b[:i]+b[j:])
                    i = j
            return b
        
        #@lru_cache(None)
        def dfs(b, h):
            b = remove(b)
            if b and not h: return float('inf')
            if not b: return 0
            
            res = float('inf')
            for i in range(len(b)+1):
                for j in range(len(h)):
                    res = min(res, 1 + dfs(b[:i] + h[j] + b[i:], h[:j] + h[j+1:]))
            return res
        
        hand = ''.join(filter(lambda x: x in board, hand))
        res = dfs(board, hand)
        return res if res != float('inf') else -1
    
    def findMinStep1(self, board: str, hand: str) -> int:
        def update(s):
            i = 0
            while i < len(s):
                j = i
                while j < len(s) and s[j] == s[i]:
                    j += 1
                
                if j - i >= 3:
                    s = s[:i] + s[j:]
                else:
                    i += 1
            print(s)
            return s
        
        def dfs(board, hand_count):
            if not board:
                return 0
            
            res = float('inf')
            i, j = 0, 0
            
            while i < len(board):
                while j < len(board) and board[j] == board[i]:
                    j += 1
                color = board[i]
                b = 3 - (j-i)
                if hand_count[color] >= b:
                    new_board = update(board[:i] + board[j:])
                    hand_count[color] -= b
                    r = dfs(new_board,hand_count)
                    if r >= 0:
                        res = min(res, r + b)
                    hand_count[color] += b
                i = j
            
            return -1 if res == float('inf') else res
        
        hand_count = collections.Counter(hand)
        return dfs(board, hand_count)