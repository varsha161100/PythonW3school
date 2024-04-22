s1=int(input("Enter the 1st side length= "))
s2=int(input("Enter the 2nd side length= "))
s3=int(input("Enter the 3rd side length= "))

if(s1==s2 and s2==s3):
    print("This is an equilateral triangle")
elif(s1!=s2 and s2!=s3):
    print("This is an scalene triangle")
else:
    print("This is an isosceles triangle")