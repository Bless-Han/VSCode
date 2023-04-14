class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        ret = []
        step = 0
        for i in range(len(mat) * 2 - 1):
            if step < len(mat):
                left = 0
                right = step
                flag = 1
            else:
                left = 
            if temp % 2 == 0:
                left, right = right, left
                flag = -flag

            for _ in range(temp, -1, -1):
                ret.append(mat[left][right])
                left += flag
                right -= flag
            step += 1
        return ret
