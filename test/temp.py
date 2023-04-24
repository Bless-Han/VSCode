class Solution:
    def isValid(self, nums):
        nums = [x for x in nums if x != '.']
        return len(nums) == len(set(nums))
            
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # check rows
        for row in board:
            if not self.isValid(row):
                return False
        # check columns
        for col in zip(*board):
            if not self.isValid(col):
                return False
        # check 3x3 squares
        for i in (0, 3, 6):
            for j in (0, 3, 6):
                square = [board[x][y] for x in range(i, i + 3) for y in range(j, j + 3)]
                if not self.isValid(square):
                    return False
        return True