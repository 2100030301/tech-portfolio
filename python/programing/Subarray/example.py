arr = [1,2,3]

n = len(arr)
for i in range(n):
    for j in range(i, n):
        for k in range(i, j+1):
            print(arr[k], end=" ")
        print()


arr = [1,2,3]

for i in range(len(arr)):
    for j in range(i, len(arr)):
        print(arr[i:j+1])

print(n * (n + 1) // 2)