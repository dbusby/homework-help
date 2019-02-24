#!/bin/python3
# Description: Ask users for sides of triangle, outputs whether it is a valid or invalid triangle

a = int(input("Enter a value for side a: "))
b = int(input("Enter a value for side b: "))
c = int(input("Enter a value for side c: "))

#makes one side the 'large side'
if b < a > c or a < b > c:
    large = a
    if a < b > c:
        large = b
else:
    large = c

#makes one side the "smallest side"
if b > a < c or a > b < c:
    small = a
    if a > b < c:
        small = b
else:
    small = c

#makes the remaing side considered to be the "medium side"
if b > a > c or b < a < c:
    medium = a
elif a > b > c or a < b < c:
    medium = b
else:
    medium = c

if small + medium > large:
    print("This is a valid triangle")
else:
    print("This is a invalid triangle")

# --------------------------------------------------
#          Cole's Version to Teacher's Req
# --------------------------------------------------

try:
    a = int(input("Enter a value for side a: "))
    b = int(input("Enter a value for side b: "))
    c = int(input("Enter a value for side c: "))
except:
    print("you must use integers, please")
    exit(2)

#makes one side the 'large side'
if b < a > c:
    large = a
elif a < b > c:
     large = b
else:
    large = c
    
#makes one side the "smallest side"
if b > a < c:
    small = a
elif a > b < c:
    small = b
else:
    small = c
    
#makes the remaing side considered to be the "medium side"
if b > a > c:
    medium = a
elif b < a < c:
    medium = a
elif a > b > c:
    medium = b
elif  a < b < c:
    medium = b
else:
    medium = c
    

if small + medium > large:
    print("This is a valid triangle")
else:
    print("This is a invalid triangle")
