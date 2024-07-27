from collections import deque

# dq = deque()        # 정수를 관리할 deque를 선언합니다. => 빈 덱
# dq.appendleft(3)    # 맨 앞에 3을 추가합니다.
# dq.appendleft(5)    # 맨 앞에 5를 추가합니다.
# print(dq[0])        # 맨 앞에 적혀있는 숫자인 5가 출력됩니다.
# print(dq[-1])       # 맨 뒤에 적혀있는 숫자인 3이 출력됩니다.
# dq.append(9)        # 맨 뒤에 9를 추가합니다.
# print(dq[-1])       # 맨 뒤에 적혀있는 숫자인 9가 출력됩니다.
# dq.popleft()        # 맨 앞 숫자(5)를 제거합니다.
# print(dq[0])        # 맨 앞에 적혀있는 숫자인 3이 출력됩니다.
# print(len(dq))      # 원소의 개수를 출력합니다 => 2

n = int(input())
dq = deque()

for i in range(n):
    temp = input().split()

    if len(temp) > 1:
        command = temp[0]
        target = int(temp[1])

        if command == 'push_back':
            dq.append(target)
        elif command == 'push_front':
            dq.appendleft(target)
    else:
        command = temp[0]

        if command == 'pop_front':
            print(dq.popleft())
        elif command == 'pop_back':
            print(dq.pop())
        elif command == 'back':
            print(dq[-1])
        elif command == 'size':
            print(len(dq))
        elif command == 'front':
            print(dq[0])
        elif command == 'empty':
            if len(dq) == 0:
                print(1)
            else:
                print(0)