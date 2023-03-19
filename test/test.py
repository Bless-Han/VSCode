class Solution:
    def evenOddBit(self, n: int) -> list[int]:
        index = 0
        even = 0
        odd = 0
        while n > 0:
            if n & 1 == 1:
                if index % 2 == 0:
                    even += 1
                else:
                    odd += 1
            n >>= 1
            index += 1
        return [even, odd]

s = Solution()
assert s.evenOddBit(17) == [2,0]
