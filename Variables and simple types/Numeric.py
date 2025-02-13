'''
Author: Jason Shi
Date: 10-01-2025 01:29:55
Last Editors: Jason
Contact Last Editors: D23090120503@cityu.edu.mo
LastEditTime: 13-02-2025 21:14:03
'''

# integer
a = 1
print(a)
print(type(a))

b = None
print(b)
print(type(b))

# hex oct bin
hex_value1 = 0x10
hex_value2 = 0XaF
print("hex_value1:", hex_value1)
print("hex_value2:", hex_value2)

oct_value1 = 0o10
oct_value2 = 0O17
print("oct_value1:", oct_value1)
print("oct_value2:", oct_value2)

bin_value1 = 0b111
bin_value2 = 0B101
print("bin_value1:", bin_value1)
print("bin_value2:", bin_value2)

# Underscores do not affect the value itself
one_million = 1_000_000
print(one_million)

# float
af1 = 5.232345566
print("af1:", af1)
print(type(af1))

f1 = 5.12e2
print("f1:", f1)
print(type(f1))
f2 = 5e3
print("f2:", f2)

# complex
c1 = 5 + 0.2j
print("c1:", c1)
print(type(c1))

c2 = 4 - 0.3j
print("c2:", c2)
print(c1 + c2)

import cmath
# sqrt is a function in cmath, used to calculate the square root of a number
c3 = cmath.sqrt(-1)
print(c3)

