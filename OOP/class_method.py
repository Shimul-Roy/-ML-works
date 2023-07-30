class Instractor:
    def __init__(self,name, address) -> None:
        self.name=name
        self.address=address
    def display(self, subject_name):
        print(f"I am {self.name} and I teach {subject_name}")

instractor_1=Instractor('shimul','dhaka')
instractor_1.display( f)