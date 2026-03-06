"""
5. Use map() on a string to convert each character into its ASCII value
(using ord()). Print the result list.
"""

str = "Hello World!"
res = list(map(ord, str))
print(res)