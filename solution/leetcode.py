class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        FONTHALF = 1
        ENDHALF = -1
        ret = []
        a = b = 0
        for i in range(len(mat) * 2 - 1):
            if i < len(mat):
                half = FONTHALF
            else:
                half = ENDHALF
            if i % 2 == 0:

        return ret
