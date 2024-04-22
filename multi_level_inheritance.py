# class grandfather():
#     def fun1(self):
#       print("i am grandfather")

# class father(grandfather):
#    def fun2(self):
#       print("i am father")

# class son(father):
#    def fun3(self):
#       print("i am son")


# obj=son()
# obj.fun1()
# obj.fun2()
# obj.fun3()



# ***********************example 2****************************


class grandfather():

    def __init__(self,gf):
      self.gf=gf

    def fun1(self):
      print("i am grandfather {}".format(self.gf))

class father(grandfather):
   
   def __init__(self,f):
      self.f=f

   def fun2(self,f):
      print("i am father {}".format(self.f))

class son(father):
   
   def __init__(self,s):
      self.s=s
      
   def fun3(self,s):
      print("i am son {}".format(self.son))


obj=son("a","b","c")
obj.fun1()
obj.fun2()
obj.fun3()
