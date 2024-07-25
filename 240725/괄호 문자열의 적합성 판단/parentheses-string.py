import sys

temp = input()

s = []

for i in range(len(temp)):
    t = temp[i]
    if t == '(':
        s.append(t)
    elif s and t == ')':
        s.pop()
    else:
        print('No')
        sys.exit()

if s:
    print('No')
    sys.exit()

print('Yes')