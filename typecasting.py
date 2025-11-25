#3. Introduction to Python Data Types & Type Casting

#Below are the basic built-in Python data types you asked about with explanations and conversion examples.

#int (integers)
#Whole numbers, positive/negative, arbitrary precision in Python.
#Example: 42, -7.

#float (floating point)
#Real numbers with decimal point. Example: 3.14, -0.5.
#Beware floating-point precision issues (representational).

#str (strings)
#Immutable sequence of Unicode characters. Operations: slicing, concatenation, formatting.

#list
#Ordered, mutable sequence. Allows duplicates. Example: [1,2,3].
#Useful for stack/queue operations, iterative modifications.

#tuple
#Ordered, immutable sequence. Use when you want fixed collections or as keys in dict (if items are hashable).

#set
#Unordered collection of unique elements. Mutable. Good for membership, deduping.

#dict
#Key → value mapping. Keys must be hashable (immutable like int, str, tuple). Values can be any object.



#Type Casting / Conversions (with examples & gotchas)
#int(), float(), str()

# int() from float truncates toward zero
print(int(3.9))   # 3
print(int(-3.9))  # -3

# float() from int or string
print(float(5))       # 5.0
print(float("3.14"))  # 3.14

# int() from string requires integer string
print(int("42"))      # 42
# int("3.14") would raise ValueError

# str()
print(str(100))       # "100"
print(str(3.14))      # "3.14"





#list(), tuple(), set()

# Strings are iterable -> list(tuple) of chars
print(list("hello"))    # ['h', 'e', 'l', 'l', 'o']
print(tuple([1,2,3]))   # (1,2,3)

# set() removes duplicates
print(set([1,2,2,3]))   # {1,2,3}

# Converting list of pairs to dict
pairs = [("a", 1), ("b", 2)]
print(dict(pairs))      # {'a':1, 'b':2}



#Quick Reference Table (Complexities):

#Linear search: O(n) time, O(1) space
#Binary search: O(log n) time, O(1) iterative / O(log n) recursive space
#dict lookup/insert/delete: average O(1) time
#set membership/insert/delete: average O(1) time

#Conversions:
#list(s) is O(len(s)) for iterables
#set(list) costs O(n)