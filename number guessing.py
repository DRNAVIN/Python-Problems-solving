import random
n=int(input("enter a number:"))
for i in range(random.randrange(0,9)):
    if(i==n):
        print("SUCESS")
    else:
        print("try again")
