# a = 5
# b = 10
# if a * 2 == b:
#     print("Equal")
# elif b % 2 == 0:
#     print("Even")
# else:
#     print("None")
# x = 12
# if x > 2:
#     if x < 10:
#         print("A")
#     else:
#         print("B")
# else:
#     print("C")

# a = 10
# b = 20
# c = 30
# if a > b: 
#     # false
#     if b > c:
#         print("1")
#     elif a > c:
#         print("2")
#     else:
#         print("3")
# else:
#     if b < c:
#         print("4")
#     else:
#         print("5")



# Q5.
# Write a Python program that:

# Takes 3 marks as input.

# Prints:

# "Excellent" if average > 90

# "Good" if between 75 and 90

# "Average" if between 50 and 75

# "Fail" otherwise

maths = int(input("Enter marks of Maths: "))
eng= int(input("Enter marks of eng: "))
sci = int(input("Enter marks of sci: "))




average = (maths + eng+ sci)/3

if average > 90:

    print("Excellent")
elif average >=75 and average<=90:
    print("Good")
elif average > 50 and average <=75:
    print("Average")
else:
    print("Fail")
