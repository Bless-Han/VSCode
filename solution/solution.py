class Solution:
    def findMinimumTime(self, tasks: list[list[int]]) -> int:
        intervals = []
        for task in tasks:
            intervals.append((task[0], task[2]))  # 添加任务开始时间和持续时间
            intervals.append((task[1], -task[2]))  # 添加任务结束时间和持续时间的负数

        intervals.sort()  # 将时间区间按照时间顺序排序

        ans = 0
        curr_time = 0
        for time, duration in intervals:
            ans += max(0, time - curr_time)  # 如果当前时间小于任务开始时间，需要等待
            curr_time = time
            ans += duration  # 执行当前任务所需的时间

        return ans

tasks = [[2,3,1],[4,5,1],[1,5,2]]
tasks = [[1,3,2],[2,5,3],[5,6,2]]
s = Solution()
print(s.findMinimumTime(tasks))
