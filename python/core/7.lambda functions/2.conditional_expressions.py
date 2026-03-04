# 6. Write a lambda to check if a number is positive, negative, or zero.
check_num = lambda x : "Positive" if x>0 else "Negative" if x<0 else "Zero"
print(check_num(-3))

# 7. Write a lambda to return the larger of three numbers.
mx = lambda a,b,c: max(a,b,c)
print(mx(3,8,2))

# 8. Write a lambda to reverse a string.
rev = lambda str: str[::-1]
print(rev("Rishita"))

# 9. Write a lambda to find length of a string.
lngth = lambda str : len(str)
print(lngth("Laghuvarapu"))

# 10. Use lambda inside a normal function.
def fun(func,n):
    return func(n)
print(fun(lambda x : x*5, 7))