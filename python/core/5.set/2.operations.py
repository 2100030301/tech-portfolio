# 6. Add an element to a set.
st1 = {3,1,7,1,4,8,2,6}
st1.add(9)
print(st1)

# 7. Add multiple elements to a set.
st2 = {1,2}
st2.update([3,4,5])
print(st2)

# 8. Remove an element using remove().
st3 = {1, 2, 3}
st3.remove(3)
print(st3)

# 9. Remove an element using discard() and show the difference.
st4 = {4,5,6}
st4.discard(8) # No error
print(st4)

# 10. Clear all elements from a set.
st5 = {2,4,6}
st5.clear()
print(st5)