class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        seen = set()
        square = 0
        for r in range(9):
            for c in range(9):
                value = str(board[r][c])

                if value == ".":
                    continue

                rowL = ("row",r, value)
                colL = ("col",c, value)
                squareL = square_label = ("square",r // 3, c // 3, value)

                if rowL in seen or colL in seen or squareL in seen:
                    return False

                seen.add(rowL)
                seen.add(colL)
                seen.add(squareL)
        return True
                    






        