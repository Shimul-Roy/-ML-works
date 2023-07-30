class calculator:
    def __init__(self,a,b) -> None:
        self.a=a
        self.b=b
    def add(self):
        return self.a+self.b
    def sub(self):
        return self.a-self.b
calc=calculator(444,69)
s=calc.add()
print(s)