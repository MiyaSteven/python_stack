# Basic - Print all integers from 0 to 150.
y = 0
while y <= 150:
    print(y)
    y = y + 1

# Multiples of Five - Print all the multiples of 5 from 5 to 1,000
x = 5
while x < 1001:
    print(x)
    x = x + 5

# Counting, the Dojo Way - Print integers 1 to 100. If divisible by 5, print "Coding" instead. If divisible by 10, print "Coding Dojo".
j = 0
txt = "Coding"
while j < 101:
    if j % 5 == 0:
        print(txt)
        j + 1
    if j % 10 == 0:
        print(txt + "Dojo")
    else:
        print(j)
j + 1

# Whoa. That Sucker's Huge - Add odd integers from 0 to 500,000, and print the final sum.
z = 0
sum = 0
while z < 500000:
    if z % 2 != 0:
        sum = sum + z

# Countdown by Fours - Print positive numbers starting at 2018, counting down by fours.
count = 2018
while count > 0:
    if count % 2 == 0:
        print(count)

# Flexible Counter - Set three variables: lowNum, highNum, mult. Starting at lowNum and going through highNum, print only the integers that are a multiple of mult. For example, if lowNum=2, highNum=9, and mult=3, the loop should print 3, 6, 9 (on successive lines)
lowNum = 1
highNum = 99
mult = 3

validNum = 0
while lowNum < highNum:
    if lowNum/mult == validNum:
        print(lowNum)
        lowNum + 1
