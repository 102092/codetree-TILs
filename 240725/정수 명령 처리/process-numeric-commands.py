class Stack:
    def __init__(self):          # 빈 스택 하나를 생성합니다.
        self.items = []
                
    def push(self, item):        # 스택에 데이터를 추가합니다.
        self.items.append(item)
                
    def empty(self):
        if self.items:
            return 0     # 스택이 비어있으면 True를 반환합니다.
        return 1
                
    def size(self):              # 스택에 있는 데이터 수를 반환합니다.
        return len(self.items)
        
    def pop(self):               # 스택의 가장 위에 있는 데이터를 반환하고 제거합니다.
        if self.size() == 0:
            raise Exception("Stack is empty")
            
        return self.items.pop()
                
    def top(self):               # 스택의 가장 위에 있는 데이터를 제거하지 않고 반환합니다.
        if self.empty():
            raise Exception("Stack is empty")
                        
        return self.items[-1]

n = int(input())
s = Stack()

for i in range(n):
    temp = input().split()

    if len(temp) > 1:
        command = temp[0]
        target = int(temp[1])
        s.push(target)

    else:
        command = temp[0]
        if command == 'top':
            print(s.top())
        elif command == 'size':
            print(s.size())
        elif command == 'pop':
            print(s.pop())
        elif command == 'empty':
            print(s.empty())