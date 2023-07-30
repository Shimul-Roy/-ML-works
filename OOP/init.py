class instractor:
    def __init__(self,ins_name, ins_address) -> None:
        self.name=ins_name
        self.address=ins_address
        self.follower=0

instractor1=instractor('shimul','rangpur')
instractor2=instractor('fsdfs','dhaka')
print(instractor1.name, instractor1.follower)
print(instractor2.name, instractor2.address)
