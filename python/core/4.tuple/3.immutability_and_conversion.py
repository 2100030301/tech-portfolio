# 11. Write a program to convert a tuple to a list, modify one element, then convert it back to a tuple.
tpl1 = (1,2,3,4,5,6)
lst=list(tpl1)
print(lst)

# 12. Write a program to delete an entire tuple and try printing it.
tpl2= (7,8,9,10,11,12)
del tpl2
print(tpl2) # This will raise a name error

# 13. Write a program to show that tuples are immutable by attempting to change an element.
tpl1[3] = 9 # This will raise typeError
print(tpl1)