# expressions are basically anything combined
# orders of operation

a=2 # this is not pythonic!
b = 5
c = 1

# Default OOO
result1 = a + b + c
print("a + b + c = ", result1)

# With parentheses: addition first
result2 = (a + b) * c
print("(a + b) * c = ", result2)

# With parentheses: division
result3 = a + (b / c)
print("a + (b / c) = ", result3)

# With parentheses: multiplication
result4 = a * b * c
print("a * b * c = ", result4)