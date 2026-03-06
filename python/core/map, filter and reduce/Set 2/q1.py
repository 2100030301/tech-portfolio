"""
1. Explain the difference between map(), filter(), and reduce() in Python.
• What does each function return?
• When should you prefer lambda functions over normal functions?
"""

"""
1. Difference between map(), filter(), and reduce() in Python

| Function       | Purpose                                                                      | What it Returns                                                                         | Example                                         |
| -------------- | ---------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | ----------------------------------------------- |
| map()          | Applies a function to every element of an iterable                           | Returns a **map object (iterator)** containing transformed values                       | `map(lambda x: x*2, [1,2,3])` → `[2,4,6]`       |
| filter()       | Selects elements that satisfy a condition                                    | Returns a **filter object (iterator)** containing only elements that pass the condition | `filter(lambda x: x%2==0, [1,2,3,4])` → `[2,4]` |
| reduce()       | Applies a function cumulatively to reduce the iterable to a **single value** | Returns **one final result**                                                            | `reduce(lambda x,y: x+y, [1,2,3,4])` → `10`     |

Note: reduce() is available in the functools module.
"""
from functools import reduce

nums = [1, 2, 3, 4]

# map()
m = list(map(lambda x: x*2, nums))
print(m)   # [2, 4, 6, 8]

# filter()
f = list(filter(lambda x: x%2==0, nums))
print(f)   # [2, 4]

# reduce()
r = reduce(lambda x, y: x+y, nums)
print(r)   # 10
"""
Use lambda functions when:

1. The function is **small and simple**.
2. The function is used **only once (temporary use)**.
3. It is needed as an **argument to functions like `map()`, `filter()`, or `reduce()`**.

list(map(lambda x: x*x, [1,2,3]))

Use a **normal function (`def`)** when:

* The function is **complex**.
* It needs **multiple statements**.
* It will be **reused in multiple places**.

* `map()` → transforms elements.
* `filter()` → selects elements based on condition.
* `reduce()` → combines elements into a single value.
* **Lambda functions** are best for short, one-time operations.

"""