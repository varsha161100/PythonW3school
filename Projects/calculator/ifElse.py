def calculator(n,x,y):
    if n==1:
        print("result =",x+y)
    elif n==2:
        print("result =",x-y)   
    else:
        print("Invalid selection!!!")

x= int(input("Enter 1st number: "))
y= int(input("Enter 2nd number: "))


print("----------------------------------------------")
print("Select any one option")
print("----------------------------------------------")
print("1. Addition")
print("2. Subtraction")
print("----------------------------------------------")

n=int(input("select any one options form above: "))

calculator(n,x,y)