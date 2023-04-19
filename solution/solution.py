class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        RIGHT = 0
        DOWN = 1
        LEFT = 2
        UP = 3
        x = y = 0
        state = RIGHT
        x_len = len(matrix)
        y_len = len(matrix[0])
        visited = [[False] * y_len for _ in range(x_len)]
        ans = []
        while matrix[x][y] == False:
            ans.append(matrix[x][y])
            visited[x][y] = True
            match state:
                case RIGHT:
                    if x + 1 == x_len or visited[x+1][y]:
                        y += 1
                        state = DOWN
                    else:
                        x += 1
                case DOWN:
                    if y + 1 == y_len or visited[x][y+1]:
                        x -= 1
                        state = LEFT
                    else:
                        y += 1
                case LEFT:
                    if x == 0 or visited[x-1][y]:
                        y -= 1
                        state = UP
                    else:
                        x -= 1
                case UP:
                    if visited[x][y-1]:
                        x += 1
                        state = RIGHT
                    else:
                        y -= 1
        return ans

RIGHT = 0
DOWN = 1
right = 0
a = RIGHT
match a:
    case right: print("is 0")
    case 1: print("is 1")
