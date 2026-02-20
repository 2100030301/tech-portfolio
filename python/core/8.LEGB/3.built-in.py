# 11. Override a built-in function name.
len = 100
print(len)

# 12. Show how to access original built-in after overriding.
import builtins
print(builtins.len([1, 2, 3]))

# 13. Demonstrate built-in scope lookup.
print(abs(-5))

# 14. Create variable named len and observe behavior.
len = 10
#  print(len([1,2]))  # Error

# 15. Restore built-in function after shadowing.
del len
print(len([1, 2, 3]))