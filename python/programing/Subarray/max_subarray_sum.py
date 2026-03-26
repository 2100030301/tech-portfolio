arr = [1,21,-3,2,-4,5]
maxarr=[]
maxsum=cursum=arr[0]

for i in range(1,len(arr)):
    cursum=max(arr[i],cursum+arr[i])
    maxsum=max(maxsum,cursum)
print(maxsum)