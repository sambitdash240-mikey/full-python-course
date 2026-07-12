# dictionary ...
# name={
#     "sambeet":100,
#     "sandeep":90,
#     "popu":87

# }
# print(name)
# print(name["sambeet"])
# print(name.keys())
# print(name.values())
# # print(name.type())
# name.update({"sambeet":99,"skd":98,"nso":76})
# print(name)
# print(name.get("sambeet"))

# methods...
# 1.name.keys()
# 2.name.values()
# 3.name.update()
# 4.name.get()
# 5.name.clear()
# 6.name.pop()
# 7.name.popitem()
# 8.name.fromkeys()


# 2...2....
# car={
#     "name":'bmw',
#     "price":8000000,
#     "year":1991
# }
# print(car)
# print(car["name"])
# # ,by using it ,if any mistake is made by us then it will return error
# print(car.keys())
# print(car.values())
# print(car.get("price"))
# # , by using it ,if any mistake is made by us then it will return none
# car.update({"new price":9000000})
# print(car)
# print(car.items()) 
# car.pop("name")
# print(car)
# print(car.popitem())
# print(car.clear())

# skd=["smabeet","sandeep","ankit"]
# b=dict.fromkeys(skd,90)
# print(b)
# it is used when we want to store the same value for each keys




# SETS..........
# a={1,2,3,4,5,"sambeet"}
# e=set()
# a.add("skd")
# print(a)

# a={1,4,3,67,"skd","pkd",45,65}
# print(a)
# b=len(a)
# print(b)
# a.remove(4)
# print(a)
# a.pop()
# print(a)
# a.clear()
# print(a)

# union....
# a={1,2,3,4}
# b={3,4,5,6}
# c=a.union(b)
# print(c)

# # intersection....
# a={1,2,3,4,5}
# b={2,3,4,5,6}
# c=a.intersection(b)
# print(c)

# # update...
# a={1,4,3,67,"skd","pkd",45,65}
# a.update(["ram"])
# print(a)

# # issubset()....
# a={1,2,3,4,5}
# b={2,3,4,5,6}
# c=a.issubset(b)
# print(c)

# a={1,2}
# b={1,2,3,4}
# c=a.issubset(b)
# print(c)


# # issuperset().....
# a={1,2,3,4,5}
# b={2,3,4,5,6}
# c=a.issuperset(b)
# print(c)

# a={1,2}
# b={1,2,3,4}
# c=b.issuperset(a)
# print(c)
