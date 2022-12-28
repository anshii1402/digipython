x = 1, 2, 3, 3, 54, 5
print(x)
print(type(x))

# assignment in python
a, b = 10, 20 # 2 values are stored in 2 variables
print(a, b)
a = 10, 20 # 2 values are packed in 1 variable as tuple
print(a, type(a))

# special case
x, x2, x3, *y = 1, 2, 3, 3, 54, 5 # x stores 1, x2 stores 2, x3 stores 3, y stores 3, 54, 5
print(type(x), type(y))