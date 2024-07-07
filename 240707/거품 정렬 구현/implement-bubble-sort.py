n = int(input())
arr = list(input().split(' '))

while True:
    sorted = True
    for i in range(n - 1):
        if int(arr[i]) > int(arr[i + 1]):
            arr[i], arr[i + 1] = arr[i + 1], arr[i]
            sorted = False
    if sorted:
        break

print(' '.join(map(str, arr)))