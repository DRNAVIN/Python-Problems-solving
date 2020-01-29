num = int(input("Enter a Range"))
def even(x):
    return x%2==0
def odd(x):
    return x%2!=0
m = filter(even,list(range(num)))
n = filter(odd,list(range(num)))
print("Even Numbers : ",list(m))
print("Odd Numbers : ",list(n))
