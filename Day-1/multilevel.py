class GF:
         def sample(self):
                  print("i am from Grand Father class")
class F(GF):
         def hello(self):
                  print("i am from Father class")
class C(F):
         def hi(self):
                  print("i am from child class")
                  
