#    multiple inheritance 
# class employee:
#     name="sambeet"
#     dep="cse"

#     def son(self):
#         print(f"the name is {self.name} and the dep is {self.dep}")
# class student:
#     nickname="sandeep"
#     sec="a"
#     roll=111

#     def skd(self):
#         print(f"the name is {self.nickname} ,sec {self.sec} ,roll {self.roll}")

# class popu(employee,student):
#     company="skd"
#     def null(self):
#         print(f"the company {self.company}")

# a=popu()
# print(a.sec,a.dep,a.roll,a.company)
# a.son()
# a.skd()
# a.null()

# # multilevel inheritance.......
# class boss1:
#     a=1

# class boss2(boss1):
#     b=2

# class boss3(boss2):
#     c=3

# d=boss3()
# print(d.a,d.b,d.c)

# e=boss2()
# print(e.a,e.b)

# # if we use  a simple{} __init__()} function within the MI then we are capable of calling only
# #  that function, which function is writting inside that class 
# class boss1:
#     a=1
#     def __init__(self):
#         print("hello boss1")

# class boss2(boss1):
#     b=2
#     def __init__(self):
#         print("hello boss2")

# class boss3(boss2):
#     c=3
#     def __init__(self):
#         print("hello boss3")

# d=boss3()
# print(d.a,d.b,d.c)

# e=boss2()
# print(e.a,e.b)

# g=boss1()
# print(g.a)

# multilevel inheritance with {super().__inti__()}.....

# class bmw:
#     name="sambeet"
#     def __init__(self):
#         print(f"the name :{self.name}")

# class od(bmw):
#     name2="skd"
#     def __init__(self):
#         print(f"the name :{self.name2}")

# class farari(od):
#     name3="pkd"
#     def __init__(self):
#         super().__init__()
#         print(f"the name:{self.name3}")

# a=farari()
# print(a.name3,a.name2)        

# class methods......

# class employee:
#     name="sambeet"
#     @classmethod
#     def show(self):
#         print(f"the class attribute is {self.name}")

# a=employee()
# a.name="sandeep"
# print(a.name)
# a.show()

# operator overlode.......

# class math:
#     def __init__(self,n):
#         self.n = n

#     def __add__(self,num):
#         print(f"the sum is {self.n+num.n}")
#     def __sub__(self,num):
#         print(f"the sum is {self.n-num.n}")
#     def __mul__(self,num):
#         print(f"the sum is {self.n*num.n}")
#     def __truediv__(self,num):
#         print(f"the sum is {self.n/num.n}")



# a=math(1)
# b=math(2)
# print(a+b)
# print(a-b)
# print(a*b)
# print(a/b)

# practice set.....

# class twodvector:
#     def __init__(self,i,j):
#         self.i=i
#         self.j=j

#     def show(self):
#         print(f"{self.i}i+{self.j}j")
# class threedvector(twodvector):
#     def __init__(self,i,j,k):
#         super().__init__(i,j)
#         self.k=k

#     def show(self):
#         print(f"{self.i}i+{self.j}j+{self.k}k")

# a=twodvector(2,3)
# b=threedvector(2,3,4) 
# a.show()
# b.show()             
        

# 2.....

# class complex:
#     def __init__(self,a,b):
#         self.a=a
        
        

#     @property    
#     def __add__(self,num):
#         return self.a+num.a
        
    
#     def show(self):
#         print(f"{self.a}+{self.b}j")

# class complexn(complex):
#     def __init__(self,a,b):
#         super().__init__(a,b)
#         self.b=b

#     def __mul__(self,num):
#          return self.b+num.b
    
#     def show(self):
#         print(f"{self.a}*{self.b}j")

# s=complexn(8,7)
# s.show()
