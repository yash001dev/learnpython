#Generating Random Value In Python
import random
members=['john','Mary','Bob','Mosh','Yash','Js']
leader=random.choice(members)
print(leader)

#Roll Dice
#Create Class Dice and add methods roll
class Dice:
    def roll(self):
        first=random.randint(1,6)
        second=random.randint(1,6)
        return first,second#It returns Tuple

dice=Dice()
print(dice.roll())
