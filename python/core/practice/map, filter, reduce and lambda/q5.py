# Use map() on a string to convert each character into its ASCII value (using ord()). Print the result list.
k = list(map(ord,input()))
l = list(map(chr, map(int,input().split())))
print(k)
print(l)