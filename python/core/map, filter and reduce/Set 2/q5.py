"""
5.  Consider the code below:
nums = [[1, 2], [3, 4], [5, 6]] result = list(map(lambda x: x.append(10), nums))
print("Result:", result) print("Nums:", nums)
Questions
• What will be the output of result?
• What will be the output of nums?
• Why does map() behave this way with list.append()?
• How can you modify the lambda so that nums is not changed?
"""

nums = [[1, 2], [3, 4], [5, 6]]
res = list(map(lambda x: x.append(10), nums))
print(f'Result:{res}')
print(f'Nums:{nums}')

"""
3. Why map() behaves this way with list.append()

map():

Applies the function to each element.

Stores whatever the function returns.

But:

list.append() returns None

It modifies the list directly

Therefore:

nums is modified

result becomes [None, None, None]

4. How to modify the lambda so that nums is NOT changed

Create a new list instead of modifying the existing one.

Correct approach
nums = [[1, 2], [3, 4], [5, 6]]

res = list(map(lambda x: x + [10], nums))

print("Result:", res)
print("Nums:", nums)
Output
Result: [[1, 2, 10], [3, 4, 10], [5, 6, 10]]
Nums: [[1, 2], [3, 4], [5, 6]]
Reason
x + [10] creates a new list instead of modifying the original one.
"""