class calculator:
    def __init__(self,a,b) -> None: #class constractor
        self.a=a
        self.b=b
        print("this is the ultimate s")
    def add(self):
        return self.a+self.b
    def sub(self):
        return self.a-self.b
calc=calculator(444,69)  #object creationf
s=calc.add()
print(type(calc))