a = "two"
b = a
c = a
print(c, end=" ")
c = "one"
b = c
a = "three"
print(a, end=" ")
print(c)