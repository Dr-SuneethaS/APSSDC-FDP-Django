class Const:
         def __init__(self,name,age):# set to be locally
                  self.name=name
                  self.age=age
                  print(self.name,self.age)
         def mydata(self):
                  print("my name {},my age is {}".format(self.name,self.age))
