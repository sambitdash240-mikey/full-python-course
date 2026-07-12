# 1....
# f=open("skd.py/file i/o.py/skd.txt","r")
# u=f.read()
# if "twinkle" in u:
#     print("true")
#     print(u)
# f.close()    

# 2....
def game():
    import random
    input("your playing a game")
    score=random.randint(1,100)
    return score
def read_score(filename):
    try:
        with open(filename,"r") as f:
           d=f.read().strip()
           if d==" ":
            return 0
           return int(d)
    except FileNotFoundError:
        return 0

def write_score(filename,score):
    with open(filename,"w") as f:
        f.write(str(score) )

filename="skd.txt"
skd_score=read_score(filename) 
print(f"your score   {skd_score}") 
score=game()
print(f"your score  {score}")


if(score > skd_score):
    write_score(filename,score)
    print(f"the score:  {score}")
else:
    print("no score is created")

