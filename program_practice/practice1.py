# x=input("enter first name:-")
# y=input("enter last name:-")

# print("My name is "+x+" "+y)

# -------------------------------------------------

# n=input("Enter the numbers with comas:-")
# a=n.split(",")

# print(a)

# ---------to accept a filename form the user and print the extension of that----------------

# file=input("enter the file name:-")
# e=file.split(".")
# print("file extention is "+e[-1])

# ----------display first and last----------

# a=["red","green","white","black"]
# size=len(a)
# print("first element: "+a[0])
# print("last element"+a[size-1])

# -------print given date----------

# date=(15,11,2024)
# print("given date is %i,%i,%i"%date)

# --- sample --- 
# 6,
# 66
# 666  and we have to add these three numbers:-

# a=print("Enter number")
# n1=int("%i"%a)
# n2=int("%i%i"%(a,a))
# n3=int("%i%i%i"%(a,a,a))

# sum=n1+n2+n3
# print("Sum =",sum)

#--------python--------------

# import calendar

# y=int(input("enter the year: "))
# m=int(input("enter the month"))

# print(calendar.month(y,m))

# -----calculate no of days between two dates

# from datetime import date
# first_date=date(2023,5,5)
# sec_date=date(2023,6,6)

# days=sec_date-first_date

# print(days)


# ----test weather a no with in 100 to 1000----

# n=115

# if n in range(100,200):
#     print("yes num is in between 100 and 200")
# else:
#     print("No, num is not in the range")
    
# ------------odd and even no------------------

# n=int(input("Enter any number"))

# if (n%2==0):
#     print("Enter number is an even no")
# else:
#     print("Enter number is an odd")

# --------count 4 in the given list-----------


# def countt(n):
#     count=0
#     for i in n:
#      if (i==4):
#         count=count+1
#     return count

# a=[44,6,2,6,4,8,1,4,99,45]

# # print(countt(a))
# # or

# print(a.count(4))

# ------------add the list 

# a=set(['red','green','red','orange'])
# b=set(['green', 'pink','orange', 'black', 'blue'])
# print(a)
# print(b)
# c=a.difference(b)
# print(c)









