class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row=defaultdict(set)
        col=defaultdict(set)
        subbox=defaultdict(set)
        
        for i in range(9):
            for j in range(9):
                if board[i][j]=='.':
                    continue
                else:
                    if board[i][j] in row[i] or  board[i][j] in col[j] or  board[i][j] in subbox[(i // 3, j // 3)]:
                        return False
                    row[i].add(board[i][j])
                    col[j].add(board[i][j])
                    subbox[(i // 3, j // 3)].add(board[i][j])
        return True

        