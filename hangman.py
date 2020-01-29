import random
mylist = [" "," "," "," "," "] #enter the strings
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
