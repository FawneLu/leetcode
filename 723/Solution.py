#723 Candy Crush
class Solution:
    def candyCrush(self, board: List[List[int]]) -> List[List[int]]:
        def getCandiesToCrush(start_r, start_c, board, val):
            count_row = 0
            for j in range(start_c,len(board[0])):
                if board[start_r][j] == val:
                    count_row += 1
                    candyToCrush.append([start_r,j])
                else:
                    break
            if count_row < 3:
                for i in range(count_row):
                    candyToCrush.pop()
            
            count_col = 0
            for i in range(start_r,len(board)):
                if board[i][start_c] == val:
                    count_col += 1
                    candyToCrush.append([i,start_c])
                else:
                    break
                    
            if count_col < 3:
                for i in range(count_col):
                    candyToCrush.pop()
                
            
                    
#BFS(不满足行列必须大于等于3的条件)            
#             candyToCrush.append([row,col])
#             count = 1
#             queue =  collections.deque()
#             queue.append([row,col])
            
#             directions = [(0,1),(0,-1),(-1,0),(1,0)]
            
#             while queue:
#                 r,c = queue.popleft()
#                 visited.add((r,c))
                
#                 for d in directions:
#                     n_r = r+d[0]
#                     n_c = c+d[1]
#                     if n_r >= 0 and n_r < len(board) and n_c >= 0 and n_c < len(board[0]) and board[n_r][n_c] == val and (n_r,n_c) not in visited:
#                         count += 1
#                         candyToCrush.append([n_r,n_c])
#                         queue.append((n_r,n_c))
            
            
                
#             if count<3:
#                 for i in range(count):
#                     candyToCrush.pop()
    
        
        def  eliminateCandies(board):
            for candy in candyToCrush:
                board[candy[0]][candy[1]] = 0
                
        
        def dropCandies(board):
            for j in range(len(board[0])):
                top, bottom = len(board)-1, len(board)-1
                while top >= 0:
                    if board[top][j] != 0 :
                        board[bottom][j],board[top][j] = board[top][j],board[bottom][j]
                        bottom -= 1
                    top -= 1
                
                    
            
        
        m,n = len(board), len(board[0])
        candyToCrush = []
        visited = set()
        
        for i in range(m):
            for j in range(n):
                if board[i][j] != 0:
                    getCandiesToCrush(i, j, board, board[i][j])
        
        
        #print(candyToCrush)
        
        if not candyToCrush:
            return board
        
        eliminateCandies(board)
        dropCandies(board)
        
        return self.candyCrush(board)