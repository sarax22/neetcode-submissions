class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        #divide board into 9 sublists (3 items in each) 
        #check if there are duplicate digits

        #check all rows
        for i in board:
            duplicates = set()
            for j in i:
                if j == ".":
                    continue

                if j in duplicates:
                    return False
                else:
                    duplicates.add(j)
        
        #check all columns
        for c in range(9):
            duplicates = set()
            for r in range(9):
                char = board[r][c]
                if char == ".":
                    continue
                if char in duplicates:
                    return False
                duplicates.add(char)
        

        # 3. Check all 3x3
        # These outer loops choose the starting (top-left) row and col of each 3x3 box
        for square in range(9):
            seen = set()
            for i in range(3):
                for j in range(3):
                    row = (square//3) * 3 + i
                    col = (square % 3) * 3 + j
                    if board[row][col] == ".":
                        continue
                    if board[row][col] in seen:
                        return False
                    seen.add(board[row][col])
        return True
