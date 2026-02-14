# 14. Write a program to access an element inside a nested tuple.
tpl1 = (1,2,(3,4),5)
print(tpl1[2][1])

# 15. Write a program to print all elements of a nested tuple using loops.
tpl2 = (1,(3,5),2,4,6,(7,8,9))
for i in tpl2:
    if isinstance(i,tuple):
        for x in i:
            print(x,end=" ")
    else:
        print(i,end=" ")
print()
# 16. Given a nested tuple of student records, print each student’s name and marks.
students = (("Rishi",20),("Valli",18),("Sreya",19))
for name,marks in students:
    print("Name :",name,", Marks :",marks)