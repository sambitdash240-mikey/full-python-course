# if ..else...
# age=int(input("enter your age:"))

# if(age>=18):
#     print("your are eligible for voting")
# else:
#     print("your  not eligible for voting")


# # if ..else..if(elif)...
# age=int(input("enter the age:"))

# if(age>=18 and age<=50):
#     print("you allowed to drive the car")

# elif(age<0):
#     print("why are you enterng the wrong age")
# elif(age>50):
#     print("you are very old to drive")
# else:
#     print("your not allowed to drive")

# 1...
# a=int(input("enter the number:"))
# b=int(input("enter the number:"))
# c=int(input("enter the number:"))
# d=int(input("enter the number:"))

# if(a>b and a>c and a>d):
#     print("a is the greatest number")
# elif(b>a and b>c and b>d):
#     print("b is the greatest")
# elif(c>a and c>b and c>d):
#     print("c is the greatest")
# else:
#     print("d is the greatest")

# or.....

# a=int(input("enter the number:"))
# b=int(input("enter the number:"))
# c=int(input("enter the number:"))
# d=int(input("enter the number:"))

# if(a>b and a>c and a>d):
#     print("a is the leargest number")
# else:
#     if(b>a and b>c and b>d):
#         print("b is the greatest num")
#     else:
#         if(c>a and c>b and c>d):
#             print("c is the greatest num")
#         else:
#             print("d is the greatest number")

# 2....
# a=int(input("enter the mark:"))
# b=int(input("enter the mark:"))
# c=int(input("enter the mark:"))
# total_mark=100
# mark=a+b+c
# pass_mark = (mark/total_mark)*100

# if(pass_mark>=40):
#     print("the student pass the exam")
# else:
#     print("fail")

# 3...
# a=input("enter the name:")
# b=int(a)

# if(len(a)<10):
#     print("it is lessthan 10")
# else:
#     print("it is fine to write")



# username = input("Enter a username: ")

# if len(username) < 10:
#     print("Valid username! It has less than 10 characters.")
# else:
#     print("Invalid username! It must be less than 10 characters.")


# 4....
a=["sambeet","sandeep","skd"]
b=input("enter the name:")

if(b in a):
    print("name is present")
else:
    print("not present")
