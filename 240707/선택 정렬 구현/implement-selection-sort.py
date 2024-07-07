n = int(input())
arr = list(input().split(' '))

for i in range(n):
    min_idx = i
    for j in range(i + 1, n):
        if int(arr[j]) < int(arr[min_idx]):
            min_idx = j
    arr[i], arr[min_idx] = arr[min_idx], arr[i]

print(' '.join(arr))