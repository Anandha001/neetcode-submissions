class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = defaultdict(set)
        col = defaultdict(set)
        square = defaultdict(set)

        for r in range(len(board)):
            for c in range(len(board[r])):
                current_no = board[r][c]
                if current_no == ".":
                    continue
                elif current_no in row[r] or current_no in col[c] or current_no in square[(r//3, c//3)]:
                    return False

                row[r].add(current_no)
                col[c].add(current_no)
                square[(r//3,c//3)].add(current_no)
        return True
        

        