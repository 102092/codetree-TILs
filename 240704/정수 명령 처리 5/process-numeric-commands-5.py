rows = input()

l = []

for i in range(0, int(rows)):
    command = input()
    if command.startswith("push_back"):
        t = command.split(" ")[1]
        l.append(t)
    elif command.startswith("get"):
        t = command.split(" ")[1]
        print(l[int(t) - 1])
    elif command == "size":
        print(len(l))
    elif command == "pop_back":
        l.pop()