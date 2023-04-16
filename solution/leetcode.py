class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        max = max(mat)
        max_i = 0
        max_j = 0
        for i in range(len(mat)):
            for j in range(len(mat[i])):
                if mat[i][j] > max:
                    print(max_i, max_j, mat[i][j])
                    max = mat[i][j]
                    max_i = i
                    max_j = j
        return [max_i, max_j]
