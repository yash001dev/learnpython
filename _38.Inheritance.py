#Inheritance Concept Of Python

class Animal:
    def walk(self):
        print("walk")

class Dog(Animal):
    def bark(self):
        print("bark")  
class Cat(Animal):
    def be_annoyting(self):
        print("annoying")
        

dog1=Dog()
dog1.walk()
dog1.bark()