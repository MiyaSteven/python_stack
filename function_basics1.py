#Predict the output of each function

#1
def a():
    return 5
print(a()) # output will be 5


#2
def b():
    return 5
print(b()+b()) # output will be 10


#3
def c():
    return 5
    return 10
print(c()) # output will be 5

#4
def d():
    return 5
    print(10)
print(d()) # output will be 5

#5
def e():
    print(5)
x = e()
print(x) # output will be none

#6
def a(b,c):
    print(b+c)
print(a(1,2) + a(2,3)) # output will be 3 and 5

#7
def a(b,c):
    return str(b)+str(c)
print(a(2,5)) # output will be 25

#8
def a():
    b = 100
    print(b)
    if b < 10:
        return 5
    else:
        return 10
    return 7
print(a()) # output will be 100, 10

#9
def a(b,c):
    if b<c:
        return 7
    else:
        return 14
    return 3
print(a(2,3)) # output will be 7
print(a(5,3)) # output will be 14
print(a(2,3) + a(5,3)) # output will be 21

#10
def a(b,c):
    return b+c
    return 10
print(a(3,5)) # output will be 8

#11
b = 500
print(b) # output will be 500
def a():
    b = 300
    print(b)
print(b) # output will be 500
a() # output will be 300
print(b) # output will be 500

#12
b = 500
print(b) # output will be 500
def a(): 
    b = 300
    print(b)
    return b
print(b) # output will be 500
a() # output will be 300
print(b) # output will be 500


#13
b = 500
print(b) # output will be 500
def a():
    b = 300
    print(b)
    return b
print(b) # output will be 500
b=a() # output will be 300
print(b) # output will be 300


#14
def a():
    print(1)
    b()
    print(2)
def b():
    print(3)
a() # output will be 1, 3, 2


#15
def a():
    print(1) 
    x = b()
    print(x)
    return 10
def b():
    print(3)
    return 5
y = a() 
print(y) # output will be 1, 3, 5, 10
