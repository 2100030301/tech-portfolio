arr = [1,2,3,4,5]
k=11
n=len(arr)
res=[]

for i in range(0,n-1):
    for j in range(i+1,n):
        if arr[i]+arr[j]==k:
            res.append((arr[i],arr[j]))

for pair in res:
    print(pair)

arr = [1,2,3,1]
k = 3

for i in range(len(arr)):
    s = 0
    for j in range(i, len(arr)):
        s += arr[j]
        if s == k:
            print(arr[i:j+1])