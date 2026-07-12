# case manipulation

# # 1....upper()
# a="sambeet"
# print(a.upper())

# # 2....lower()
# a="SAMBEET"
# b=a.lower()
# print(b)

# # 3...title()  Capitalizes each word
# a="hello world"
# print(a.title())

# # 4...capitalize()...Capitalizes first letter
# a="sambeet"
# print(a.capitalize())

# # 5....swapcase()...Swaps upper/lower case
# a="SAMBEET kumar dash"
# print(a.swapcase())


# # find and find

# # 1...find()..to find and return the index number
# # if the item is not found then it will return -1
# a="sambeet kumar, dash"
# b=a.find(",")
# print(b)    

# n="i am a good boy"
# print(n.find("k"))

# # 2..index()..Like find() but raises error if not found

# a="sambeet"
# print(a.index("m"))

# # 3..count()..Counts occurrences of substring
# a="sambeet"
# print(a.count("m"))

# # 4...startswith()..Checks if string starts with s
# a="sambeet"
# b=a.startswith("sa")
# print(b)

# # 5..endswith()..Checks if string ends with s
# a="sambeet"
# print(a.endswith("eet"))


# trim and pad.......

# 1..strip()....Removes leading/trailing whitespace
# a="    sambeet    "
# print(a.strip())

# # # 2..lstrip()..Removes leading whitespace from left side
# # a="   sambeet   gkhj"
# # print(a.lstrip())

# # # 3...rstrip()...Removes trailing whitespace from right side
# # a="   sambeet    "
# # print(a.rstrip())

# # 4..ljust().. Left-aligns, pads with spaces
# a="   sambeet   "
# print(a.strip().ljust(5))

# # 5..rjust()..Right-aligns, pads with spaces
# a="sambeet"
# print(a.rjust(5))

# # 6..center()...Centers with padding
# a="sambeet"
# print(a.center(6))


# Replace & Split & Join

# 1..replace()..Replaces substring
# a="sambeet kumar"
# print(a)
# b=a.replace("kumar","dash")
# print(b)

# # 2...split()...Splits into a list
# a="s,a,m,b,e,e,t"
# print(a.split(","))

# # 3....join()...  Joins iterable with string
# a=["a","b","c"]
# b=",".join(a)
# print(b)

# a=["a","b","c"]
# b="|".join(a)
# print(b)