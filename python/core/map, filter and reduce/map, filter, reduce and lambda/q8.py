#  Given a list of integers, use map() with id() to print the memory address of each element. Example: [10, 350, 10, 350, 20] — explain why some addresses repeat
l = [10,350,85,120]
k = map(lambda x: id(x),l)
print(k)