def isValidSudoku_1(self, board: List[List[str]]) -> bool:
    cols = defaultdict(set)
    rows = defaultdict(set)
    squares = defaultdict(set)  # key = (r /3, c /3)

    for r in range(9):
        for c in range(9):
            if board[r][c] == ".":
                continue
            if (
                board[r][c] in rows[r]
                or board[r][c] in cols[c]
                or board[r][c] in squares[(r // 3, c // 3)]
            ):
                return False
            cols[c].add(board[r][c])
            rows[| 1 | 3 | 4 | 5 | 7 | 10 | 11 |    Target = 9

L^ ------------- R^r].add(board[r][c])
            squares[(r // 3, c // 3)].add(board[r][c])

    return True

def isValidSudoku_2(self, board: List[List[str]]) -> bool:
    rows = [[], [], [], [], [], [], [], [], []]
    col = [[], [], [], [], [], [], [], [], []]
    boxes = [[], [], [], [], [], [], [], [], []]

    for i in range(9):
        for j in range(9):
            tmp = board[i][j]
            if tmp != ".":    
                box = 3 * (i//3) + (j//3)
                if (tmp in rows[i] or 
                   tmp in col[j]  or 
                   tmp in boxes[box]):
                    return False
                col[j].append(tmp)
                rows[i].append(tmp)
                boxes[box].append(tmp)

    return True