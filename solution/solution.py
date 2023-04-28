import collections
# init
queue = collections.deque()
# add from right
queue.append((2, 99))
# add from left
queue.appendleft((9999,88888))
# pop from right
print(queue.pop())
# pop from left
print(queue.popleft())
