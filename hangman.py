import random
mylist = ["magesh","aravind","gokul","preeth","guna"]
print(mylist)
r = random.choice(mylist)
def choice():
    n = input("Guess a Name")
    if(n==r):
        print("Sucess")
    else:
        print("Try Again")
        choice()
choice()        
