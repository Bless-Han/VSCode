'''
   @pintia psid=994805260223102976 pid=994805273883951104 compiler=PYTHON3
   
   ProblemSet: PAT (Basic Level) Practice （中文）
   
   Title: 1052 卖个萌
   
   https://pintia.cn/problem-sets/994805260223102976/exam/problems/994805273883951104
   
'''
# @pintia code=start
import sys

hands = sys.stdin.buffer.readline().decode('utf-8').replace('[', '').replace('\n', '').replace(' ', '').split(']')
# eyes = sys.stdin.buffer.readline().decode('utf-8').replace('[', '').replace('\n', '').replace(' ', '').split(']')
# mouthes = sys.stdin.buffer.readline().decode('utf-8').replace('[', '').replace('\n', '').replace(' ', '').split(']')
# try:
#     hands.remove('')
# except ValueError:
#     pass
# try:
#     eyes.remove('')
# except ValueError:
#     pass
# try:
#     mouthes.remove('')
# except ValueError:
#     pass

# k = int(input())

# for i in range(k):
#     try:
#         a, b, c, d, e = map(int, input().split())
#         print(f'{hands[a - 1]}({eyes[b - 1]}{mouthes[c - 1]}{eyes[d - 1]}){hands[e - 1]}')
#     except (IndexError, ValueError):
#         print('Are you kidding me? @\/@')

# @pintia code=end