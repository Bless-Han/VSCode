class Solution:
    def miceAndCheese(self, reward1: list[int], reward2: list[int], k: int) -> int:
        def count(rew, k):
            temp = sorted(rew, reverse=True)
            return sum(temp[:k])
        if count(reward1, k) < count(reward2, k):
            reward1, reward2 = reward2, reward1
        ret = 0
        m1_i = []
        for i in range(k):
            max = 0
            curr_i = 0
            for i, r in enumerate(reward1):
                if r > max and i not in m1_i:
                    max = r
                    curr_i = i
            m1_i.append(curr_i)
            ret += max
        for i in sorted(m1_i, reverse=True):
            reward2.pop(i)
        m2_i = []
        for i in range(k):
            max = 0
            curr_i = 0
            for i, r in enumerate(reward2):
                if r > max and i not in m2_i:
                    max = r
                    curr_i = i
            m2_i.append(curr_i)
            ret += max
        return ret

reward1 = [1,1]
reward2 = [1,1]
k = 2
reward1 = [4,1,5,3,3]
reward2 = [3,4,4,5,2]
k = 3
print(Solution().miceAndCheese(reward1, reward2, k))
print("Ok")


[4,1,5,3,3]
[3,4,4,5,2]
3

12
9


