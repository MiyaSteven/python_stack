# loops with range
for x in range(0, 10, 1):
    pass # insert what to do in each iteration
# 0 represents the value to start iterating with
# 10 represents the value to stop iterating at
# 1 represents the value in which the iterator changes per iteration

for x in range(0, 10, 1):
    pass # start iteration at 0, end when x < 10 and iterator increases by 1 each iteration

for x in range(0, 10):	# increment of +1 is implied
    pass

for x in range(10):	# increment of +1 and start at 0 is implied
    pass

for x in range(0, 10, 2):
    print(x) # output: 0, 2, 4, 6, 8

for x in range(5, 1, -3):
    print(x) # output: 5, 2

# iterate through list
my_list = ["abc", 123, "xyz"]
for i in range(0, len(my_list)):
    print(i, my_list[i]) # output: 0 abc, 1 123, 2 xyz
    
# OR 
    
for v in my_list:
    print(v) # output: abc, 123, xyz

# iterating through dictionaries / the iterator are they keys in the dictionary
my_dict = { "name": "Noelle", "language": "Python" }
for k in my_dict:
    print(k) # output: name, language

# grab the values of the keys in the dictionary
my_dict = { "name": "Noelle", "language": "Python" }
for k in my_dict:
    print(my_dict[k]) # output: Noelle, Python

capitals = {"Washington":"Olympia","California":"Sacramento","Idaho":"Boise","Illinois":"Springfield","Texas":"Austin","Oklahoma":"Oklahoma City","Virginia":"Richmond"}

# another way to iterate through the keys
for key in capitals.keys():
     print(key) # output: Washington, California, Idaho, Illinois, Texas, Oklahoma, Virginia

#to iterate through the values
for val in capitals.values():
     print(val) # output: Olympia, Sacramento, Boise, Springfield, Austin, Oklahoma City, Richmond

#to iterate through both keys and values
for key, val in capitals.items():
     print(key, " = ", val) # output: Washington = Olympia, California = Sacramento, Idaho = Boise, etc

# for loop vs while loop
for count in range(0,5):
    print("looping - ", count)
count = 0
# same output
while count < 5:
    print("looping - ", count)
    count += 1

# else statements will do something when the conditions are not met
y = 3
while y > 0:
    print(y)
    y = y - 1
else:
    print("Final else statement")

# using break 
for val in "string":
    if val == "i":
        break
    print(val) # output: s, t, r

# using continue
for val in "string":
    if val == "i":
        continue
    print(val) # output: s, t, r, n, g
# notice, no i in the output, but the loop continued after the i

y = 3
while y > 0:
    print(y)
    y = y - 1
    if y == 0:
        break
else: # only executes on a clean exit from the while loop (i.e. not a break)
   print("Final else statement") # output: 3, 2, 1
