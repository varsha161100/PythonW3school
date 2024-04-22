y=int(input("Enter any year:-"))

if y%4==0 and y%100!=0 or y%400==0:
    print(y," is an leap year.")
else:
   print(y," is not an leap year.")  