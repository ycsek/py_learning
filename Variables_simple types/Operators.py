# Assignment Operators
st = "python"
pi = 3.14
visited = True
st2 = st
print(st2)

a1 = 12.34
a2 = a1 + 10
print("a2's value is: %g" % a2)

# Arithmetic Operators
# Addition
a = 5
b = 2
the_sum = a + b
print("The sum of a and b is: %d" % the_sum)

s1 = "Hello"
s2 = "World"
s3 = s1 + s2
print(s3)
# Subtraction
c = 5
d = 2
the_diff = c - d
print("The difference of c and d is: %d" % the_diff)

x = -5.0
x = -x
print(x)

# Multiplication
e = 5
f = 2
the_product = e * f
print("The product of e and f is: %d" % the_product)

s3 = "City"
print(s3 * 5)

# Division
print("5/2 = ", 5 / 2)
print("5//2 = ", 5 // 2)

# Mod
print("5%2 = ", 5 % 2)
print("-5.2 % -3.1 = ", -5.2 % -3.1)
print("5.2 % -2.9 = ", 5.2 % -2.9)
print("-5.2 % 3.1 = ", -5.2 % 3.1)
print("5.2 % -3.1 = ", 5.2 % -3.1)

# Exponentiation
print("2**3 = ", 2**3)
print("2**-3 = ", 2**-3)
print("2**0 = ", 2**0)
print("2**0.5 = ", 2**0.5)

# Bitwise Operators
# Bitwise AND
print("5 & 9 = ", 5 & 9)
# Bitwise OR
print("5 | 9 = ", 5 | 9)
# Bitwise Negation
print("~5 = ", ~5)
# Bitwise XOR
print("5 ^ 9 = ", 5 ^ 9)
# Bitwise Left Shift
print("5 << 2 = ", 5 << 2)
# Bitwise Right Shift
print("-5 >> 2 = ", 5 >> 2)

# Boolean Operators
#! > < >= <= == != is, is not
print("5 is bigger than 3: ", 5 > 3)
print("5 is smaller than 3: ", 5 < 3)
print("5 is equal to 3: ", 5 == 3)
print("20 is greater than or equal to 20: ", 20 >= 20)
print("1 is equal to True: ", 1 == True)
print("0 is equal to False: ", 0 == False)
print("True + False = ", True + False)
print("True - False = ", True - False)


import time

y = time.gmtime()
print(y)
u = time.gmtime()
print(u)
print("y = u? ", y == u)
print("y is u? ", y is u)

# Logical Operators
#! and or not
print("not false = ", not False)

print("5 >3 and 20 > 10: ", 5 > 3 and 20 > 10)
print("4 >= 5 or c > a:", 4 >=5 or "c" > "a")

# Ternary Operators
# Syntax: [on_true] if [expression] else [on_false]
a = 5
b = 10
st3 = "a is greater than b" if a > b else "b is greater than a"
print(st3)
print("a is bigger than b" )if a > b else print("b is bigger than a")

