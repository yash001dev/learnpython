#Person Name Class It Have Two Methods name it is innermember data of class and talk
class Person:
    def __init__(self,name):
        self.name=name
    def talk(self):
        print(f"Hi I am {self.name}")
    
yash=Person("YASH N SANGHAVI")
print(yash.name)
yash.talk()

bob=Person("Bob Smith")
bob.talk()