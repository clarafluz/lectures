

# Mutable
a = [1,2,3]
print(id(a))
a[2] = 4          
print(id(a))              

# Immutable
b = 42
print(id(b))
b += 1
print(id(b))