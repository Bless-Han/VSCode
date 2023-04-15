class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        FONTHALF = 1
        ENDHALF = -1
        ret = []
        a = b = 0
        for i in range(len(mat) * 2 - 1):
            ret.append(mat[a][b])
            if i < len(mat):
                half = FONTHALF
            else:
                half = ENDHALF
            if a == 0 or b == 0:
                if a == 0 and half = FONTHALF:
                    b += 1
                elif a == 0 and half = ENDHALF:
                    a += 1
                elif b == 0 and half = FONTHALF:
                    a += 1
                elif b == 0 and half = ENDLAHF:
                    

        return ret
