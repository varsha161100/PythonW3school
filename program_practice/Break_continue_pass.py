a=[1,3,2,1,2,3,1,0,1,3]

for i in a:
    pass
    if(i==0):
        current=i
        break
    elif (i%2==0):
        continue

print(current)
print(a)
