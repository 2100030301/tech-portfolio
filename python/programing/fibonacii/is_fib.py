n = 8
a,b=0,1
x=0
while x<=n:
    c=a+b
    a=b
    b=c
    x+=1

print(n)
print(a==n)