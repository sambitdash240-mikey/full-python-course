# class student:
#     section="f" #class attribute
#     division=1
# skd=student()
# skd.name="sambeet" #instance attribute or object attribute
# print(skd.name,skd.section,skd.division)    

# rohan=student()
# rohan.name="sandeep" #instance attribute
# print(rohan.name,rohan.section,rohan.division)

# with function.......
# class student:
#     section="f" #class attribute
#     division=1

#     def popu(self):
#         print(f"the section is {self.section} ,and the division is {self.division}")
#   (staticmethod).......
#     @staticmethod
#     def moon():
#         print("good morning")    
# skd=student()
# # skd.name="sambeet" #instance attribute
# student.popu(skd) 
# student.moon()

# __init__ method.....
class employee:

    def __init__(self,name,salary,language):
        self.name=name
        self.salary=salary
        self.language=language
        print("i am very good in my work")

skd=employee("sambeet",12000,"python")
print(skd.name,skd.salary,skd.language)        
        