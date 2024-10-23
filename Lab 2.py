s = "Hello"
lst = [1, 2, 3]
tup = (1, 2, 3)
dct = {'a': 1, 'b': 2}
st = {1, 2, 3}

print("\nString Operations:")
print("String:", s)
print("Indexing:", s[1])
print("Slicing:", s[1:4])
print("Concatenation:", s + " World")
print("Repetition:", s * 2)

print("\nList Operations:")
print("List:", lst)
print("Indexing:", lst[1])
print("Slicing:", lst[1:3])
print("Concatenation:", lst + [4, 5])
print("Repetition:", lst * 2)

print("\nTuple Operations:")
print("Tuple:", tup)
print("Indexing:", tup[1])
print("Slicing:", tup[1:3])
print("Concatenation:", tup + (4, 5))
print("Repetition:", tup * 2)

print("\nDictionary Operations:")
print("Dictionary:", dct)
print("Accessing:", dct['a'])
dct['new key'] = 3
print("After addition:", dct)

print("\nSet Operations:")
print("Set:", st)
st.add(4)
print("After addition:", st)
