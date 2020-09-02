class Cont:
         def __init__(self):
                  print("i am from constructor")
         def  hello(self):
                  print("I from from hello method")

obj=Cont()
obj.hello()
obj=Cont().hello()
