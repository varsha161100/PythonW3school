x= int(input("Enter 1st number: "))
y= int(input("Enter 2nd number: "))

print("----------------------------------------------")
print("Select any one option")
print("----------------------------------------------")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("----------------------------------------------")

choice=int(input("select any one options form above: "))

if choice ==1:
    print("Result = ",x+y)
elif choice==2:
    print("Result = ",x-y)
elif choice==3:
    print("Result = ",x*y)
elif choice==4:
    print("Result = ",x/y)
else:
    print("you have selected an Invalid option!!! ")

