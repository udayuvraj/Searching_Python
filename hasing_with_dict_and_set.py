#Hashing - Using dict and set in Python
#Conceptual Explanation

#Hashing maps keys to indices using a hash function; Python hides low-level details.

#dict (hash table) maps keys → values. Average lookup/insert/delete: O(1).

#set stores unique elements. Average membership test/insert/delete: O(1).

#Both rely on objects being hashable (__hash__ and __eq__ behavior). Mutable built-ins like list are unhashable.


#1. dict - Common Uses and Examples
#Frequency counting, memoization, grouping, storing keyed records.
#Code: Basic operations & frequency counting

# Basic dict usage
person = {"name": "Asha", "age": 24}
print(person["name"])        # 'Asha'
person["city"] = "Hyderabad" # insert
print("Keys:", list(person.keys()))
print("Values:", list(person.values()))

# Frequency counting example
arr = ["apple", "banana", "apple", "orange", "banana", "apple"]
freq = {}
for x in arr:
    freq[x] = freq.get(x, 0) + 1  # get default 0 then increment
print("Frequencies:", freq)  # {'apple':3, 'banana':2, 'orange':1}

# Using dict comprehension to invert a small mapping (values must be unique)
d = {"a": 1, "b": 2}
inv = {v: k for k, v in d.items()}
print("Inverted:", inv)  # {1:'a', 2:'b'}



#Notes

#dict.get(key, default) is handy to avoid KeyError.

#defaultdict from collections simplifies counters but dict + get is fine.


#2.set - Common Uses and Examples

#Remove duplicates, membership checks, set algebra (union/intersection/difference), building adjacency checks.

#Code: Basic set operations

# Basic set usage
s = set([1, 2, 3, 2])
print("Set (duplicates removed):", s)  # {1,2,3}

# Membership test - O(1)
print("Is 2 in s?", 2 in s)

# Add / remove
s.add(4)
s.discard(2)   # discard doesn't raise error if missing
print("After changes:", s)

# Set algebra
A = {1, 2, 3}
B = {3, 4, 5}
print("Union:", A | B)            # {1,2,3,4,5}
print("Intersection:", A & B)     # {3}
print("Difference A - B:", A - B) # {1,2}

# Use-case: find duplicates in list
arr = [1,2,3,2,4,1]
duplicates = {x for x in arr if arr.count(x) > 1}  # simple (but arr.count in loop is O(n^2))
# Better: use a seen set
seen = set()
dups = set()
for x in arr:
    if x in seen:
        dups.add(x)
    else:
        seen.add(x)
print("Duplicates:", dups)  # {1,2}


#Performance tip
#Avoid arr.count(x) in loops - that makes O(n²). Use a dict/set approach for linear-time duplicates detection.

