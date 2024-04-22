# a={"name":"varsha",
#    "class":3,
#    "sub":"math",
#    "year":2343,
#    "year":2024}

# print(a)
# print(a["name"])
# print(len(a))

# x=a.get("name")
# print(x)

# z=a.keys()
# print(z)

# y=a.values()
# print(y)

# ------------add new values---------

# a["rollNo"]=141
# print(a)

# p=a.items()
# print(p)

# check keys exists or not_____________________

# if "name" in a:
#     print("yes")
# else:
#     print("No")

# change the dic values

# a["name"]="ram"

# a.update({"name":"ram"})
    
# delete

a={"name":"varsha",
   "class":3,
   "sub":"math",
   "year":2343,
   "year":2024}
    
# a.pop("name")
# del a["name"]
# del a

# for i in a.values():
#     print(i)

# for i in a.keys():
#     print(i)

# for i in a.items():
#     print(i)

# copy___________________

# b=a.copy()
# print(b)

# ___nested dic

x={"a1":{"name":"varsha","age":54},
   "b1":{"name":"rohan","age":65}
   }

# print(x)

print(x["a1"]["age"])

