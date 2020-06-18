# test = "a x a" # true
# test2 = "racecar" # true
# test3 = "Dud" # false
# test4 = "oho!" # false

# # def isPalindrome(test3):
# #     # left = str[0]
# #     # right = (len(string)-1)
# #     for i in range(0, len(test)//2):
# #         if test[i] != test[len(test)-1-i]:
# #             return False
# #     return True

# # print(isPalindrome(test3))

# def isPalindrome(test):
#     for i in range(0, len(test)//2, 1):
#         if test[i] != test[len(test)-1-i]:
#             return False
#     return True

# print(isPalindrome(test))
# print(isPalindrome(test2))
# print(isPalindrome(test3))
# print(isPalindrome(test4))


# s = "reverse me please"
# def reverse(s):
#     reversed_list = []
#     str = ""
#     for i in s:
#         str = i + str
#     reversed_list.append(str)
#     return reversed_list[0]

# print(reverse(s))

# string = "hello I work"

# string = "hello world"

# def reverse_word(string):
#     empty_list = []

#     for i in range (len(string)):
#         if string[i] != " ":
#             empty_list.append(string[i])

#     left = 0
#     right = (len(empty_list)-1)
#     print(left)
#     print(right)
#     while left != right and left < right:
#         temp = empty_list[left]

#         empty_list[left] = empty_list[right]
#         empty_list[right] = temp

#         left += 1
#         right -= 1
#     return empty_list
# print(reverse_word(string))

# string="aaaabbcddd"
# # Output: "a4b2c1d3"
# count=1
# output="string[0]"

# if len(string)>1:
#     for i in range(1, len(string)):
#         if string[i-1]==string[i]:
#             count+=1

#         else :
#             output+=count+string[i]
#             count=1
#     output += ("")
# else:
#     i=0
#     output += ("put stuff we want to see here")
# print(output)

# solution 1
# def coins(num):
#     changeLeft = num
#     if changeLeft > 24:
#         print(changeLeft//25, "quarters")
#         changeLeft = num % 25
#     if changeLeft > 9:
#         print(changeLeft//10, "dimes")
#         changeLeft = changeLeft % 10
#     if changeLeft > 4:
#         print(changeLeft//5, "nickles")
#         changeLeft = changeLeft % 5
#     if changeLeft > 0:
#         print(changeLeft//1, "pennies") # changeLeft should be 0 at this point and the prints should show how many of each coin

# print(coins(137))

# def leastCoins(num):
#     quarters = 0
#     dimes = 0
#     nickels = 0
#     pennies = 0

#     total = num

#     while total != 0:
#         if total >= 25:
#             quarters += 1
#             total -= 25

#         elif total >= 10:
#             dimes += 1
#             total -= 10
        
#         elif total >= 5:
#             nickels += 1
#             total -= 5

#         elif total >= 1:
#             pennies += 1
#             total -= 1

#     print(f"Input: {num}" )

#     print(f"Using: {quarters} quarters, {dimes} dimes, {nickels} nickels, {pennies} pennies")

# print(leastCoins(137))

# solution 1
# def make_change(num):
#     change = {
#         'quarters' : 0
#         dimes : 0
#         nickels : 0
#         pennies : 0
#     }

#     while num > 0:
#         if num >= 25:
#             change.update(quarters += 1)
#             num -25
#         elif num >= 10:
#             change.update(dimes += 1)
#             num -10
#         elif num >= 5:
#             change.update(nickels += 1)
#         else:
#             change.update(pennies += 1)
#     return change

# print(make_change(137))

# def make_change(num):
#     change = {
#     'quarters' : 0,
#     'dimes' : 0,
#     'nickels' : 0,
#     'pennies' : 0
#     }
#     changeLeft = num
#     while changeLeft > 0:
#         if changeLeft >= 25:
#             change.quarters += 1
#             changeLeft -25
#         elif num >= 10:
#             change.dimes += 1
#             num -10
#         elif num >= 5:
#             change.nickels += 1
#         else:
#             change.pennies += 1
#     return change

# print(make_change(137))

list1 = [1, 1, 2, 2, 3, 3]
# [1, 1, 2, 2, 3, 3] -> [1, 1, 2, 2, 3, 3, 1, 2, 3] -> [1, 2, 3]
def dedupe2(list1):
    # define a variable called length and set it to the length of the list1
    length = len(list1)
    # create a counter called j and start it at 1
    j = 0
    # create a for loop with counter i which iterates through our list1
    for i in list1:
        # create an if conditional statement that iterates through the old list and create a sublist
        if i not in list1[0:j]:
            # append the unique values
            list1.append(list1[i])
        if j >= length:
            break
        j += 1
    new_length = len(list1)
    difference = new_length - length
    j=0
    for item in range(length, new_length):
        list1[j] = list1[item]
        j+=1
    while len(list1) > difference:
        list1.pop() # output from this [1, 2, 3]?
    return list1
print(dedupe2(list1))