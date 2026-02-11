# 6. Create an empty list and add three numbers to it using append().
integers = []
integers.append(10)
integers.append(20)
integers.append(30)
print(integers)

# 7. Insert "Python" at index 1 in the list [languages = ["Java", "C++", "JavaScript"]
languages=["Java", "C++", "Javascript"]
languages.insert(1,"Python")
print(languages)

# 8. Extend this list with another list
lst1 = [1,2,3]
lst2 = [4,5,6]
lst1.append(lst2)
print(lst1)

# 9. Remove "apple" from this list fruits = ["apple", "banana", "cherry"]
fruits = ["apple", "banana", "cherry"]
fruits.remove("apple")
print(fruits)

# 10. Remove and print the last element from this list nums = [5, 10, 15, 20]
nums = [5, 10, 15, 20]
ele = nums.pop()
print(ele)

# 11. Remove the element at index 2 from this list letters = ["a", "b", "c", "d"]
letters = ["a", "b", "c", "d"]
letters.pop(2)
print(letters)

# 12. Clear all elements from a list
letters.clear()
print(letters)
