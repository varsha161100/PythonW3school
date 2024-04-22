#  ________________ interchange first and last element of an list_______________________


# def swapList(a):
#     size=len(a)
#  #swapping
#     temp=a[0]
#     a[0]=a[size-1]
#     a[size-1]=temp

#     return a

# a=[43,55,78,21,99]
# print(swapList(a))


def swapPos(a,pos1,pos2):
     size=len(a)
 #swapping
     temp=a[pos1-1]
     a[pos1-1]=a[pos2-1]
     a[pos2-1]=temp

     return a

a =[43,55,78,21,99]
pos1,pos2=1,3
print(swapPos(a,pos1,pos2))



