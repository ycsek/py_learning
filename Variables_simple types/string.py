'''
Author: Jason Shi
Date: 13-02-2025 21:14:16
Last Editors: Jason
Contact Last Editors: D23090120503@cityu.edu.mo
LastEditTime: 02-03-2025 12:27:16
'''

# keyword in python
import keyword
print(keyword.kwlist)

# string and eccape characters

# special string
s1 = "I'm a student."
s2 = 'My name is Jason'
s3 = s1 + s2
print(s3)

# repr and str
s4 = "My GPA is about "
g = 3.7
print(s4 + repr(g))
print(s4 + str(g))

st = "I will play my file"
print(st)
print(repr(st))

# input and raw_input
# raw_input in python 2.x, eaqul to input in python 3.x
# msg = input("Input: ")
# print(type(msg))
# print(msg)

# long string
s = '''"Let's go to the park", tom said. "OK, let's go", Mary replied. they went to the park.'''
print(s)

# bytes
# bytes is a data type in python 3.x, used to store binary data, such as images, audio, video, etc. Default encoding is utf-8
b1 = bytes()
b2 = b''
b3 = b'hello'
print(b3)
print(b3[0])
print(b3[2:4])

b4 = bytes("澳门城市大学，数据科学学院", encoding="utf-8")
print(b4)

b5 = "澳门城市大学，数据科学学院".encode("utf-8")
print("b5", b5)

# decode bytes
b6 = b5.decode("utf-8")
print("b6", b6)

# escape characters
''' 
\\: backslash
\': single quote
\n: newline
\b: backspace
\t: tab
\r: carriage return
'''

a = "Hello \n Jason \n Good Morning"
print(a)

b = "Student ID \t Name \t Age"
c = "D23090120503 \t Jason \t 20"
print(b)
print(c)

# format string
# %
SID = "D23090120503"
sname = "Jason"
print(" %s's ID is %s" %(sname,SID))

# conversion operator
'''
%d and %i: integer with sign and used to represent decimal numbers
%o : octal number
%x and %X : hexadecimal number
%e and %E : scientific notation
%f and %F : floating point number
%g and %G : Intelligent selection of %f %F or %e %E
%C : single character
%s : string
%r : string, used repr() to convert
'''

num = -27
print("num is: %6i" %num)
print("num is: %6d" %num)
print("num is: %6o" %num)
print("num is: %6x" %num)
print("num is: %6X" %num)
print("num is: %6s" %num)

num2 = 30
# minimum width is 6
print("num2 is: %06d" %num2)
# minimum width is 6 with sign
print("num2 is: %+06d" %num2)
# minimum width is 6, left alignment
print("num2 is: %-6d" %num2)

val = 3.1415926
# minimun width is 8, keep 3 decimal places
print("val is: %8.3f" %val)
# minimun width is 8, keep 3 decimal places, fill with 0 
print("val is: %08.3f" %val)
# minimun width is 8, keep 3 decimal places, fill with 0, with sign
print("val is: %+08.3f" %val)

# keep 3 characters
name = "Jason"
print("name is: %.3s" %name)
# keep 3 characters, minimum width is 10
print("name is: %10.3s" %name)

# sequence
g = "City University of Macau"
# get index equals 2 character in g
print(g[2])
# get index from 4 begin with right
print(g[-4])
# get index from 2 to 5
print(g[2:5])
# get index from 3 to fifth from last character's substring
print(g[3:-5])
# get index from beginning to 5
print(g[:5])
# check if "City" in g
print("City" in g)
# check if "City" not in g
print("City" not in g)
# get length of g
print(len(g))
# get lenght of city 
print(len("City"))

# Capitalize and lower
print(g.capitalize()) # Capitalize the first character
print(g.lower())    # Lowercase all characters
print(g.upper())    # Uppercase all characters
print(g.title())    # Capitalize the first character of each word


