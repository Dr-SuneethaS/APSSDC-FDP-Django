class A:
         def sample(self):
                  print("i am from A class")
class B:
         def hello(self):
                  print("i am from B class ")
         def mydata(self):
                  print(" i am second method in class B")
class C(A,B):
         def hi(self):
                  print("i am from C class ")

class parent:
         def func1(self):
                  print("i from parent class")
class child1(parent):
         def func2(self):
                  print("I am from child1 class")
class child2(parent):
         def func3(self):
                  print(" i am from child2 class")

class newclass(C,child2):
         def myfun(self):
                  print("i am from new class")
