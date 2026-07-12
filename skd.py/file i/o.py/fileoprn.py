# fileopen....
# f=open("skd.py/file i/o.py/openfile.txt","r")
# u=f.read()
# print(u)
# f.close()

# file..write....
# f=open("skd.py/file i/o.py/openfile.txt","w")
# f.write("but i am very good at everything")
# f.close()

# s=open("skd.py/file i/o.py/openfile.txt","w")
# s.write("i dont care")
# s.close()

# i can be written only one Time (file..write....)

# readlines....
# f=open("skd.py/file i/o.py/openfile.txt","r")
# u=f.readlines()
# print(u)
# f.close() 

# f=open("skd.py/file i/o.py/openfile.txt","r")
# line1=f.readlines()
# print(line1,type(line1))
# line2=f.readlines()
# print(line2,type(line2))
# line3=f.readlines()
# print(line3),type(line3)
# f.close()

# with while loop....
# f=open("skd.py/file i/o.py/openfile.txt","r")
# line=f.readline()
# while(line != ""):
#     print(line)
#     line+=f.readline()

# f.close()  

# .append().....
# f=open("skd.py/file i/o.py/skd.txt","a")
# f.write("mr.skd\n")
# f.close()

# with statement......
# with open ("skd.py/file i/o.py/openfile.txt") as f:
#     print(f.read())