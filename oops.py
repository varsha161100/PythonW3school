# class-------------

# class A:
#     x=34

# # print(A)

# p1=A()
# print(p1.x)


class A:
    def __init__(self, name, age):
        self.Name=name 
        self.Age=age

p1=A("varsha",88)  #//obj create

print(p1.Name)
print(p1.Age)


