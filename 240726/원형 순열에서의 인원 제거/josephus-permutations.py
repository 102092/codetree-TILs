from collections import deque

q = deque()
res = []

n, k = map(int, input().split())

for i in range(n):
    q.append(i + 1)

while q:
    for i in range(k):
        q.append(q.popleft())
    res.append(q.pop())

print(' '.join(map(str, res)))