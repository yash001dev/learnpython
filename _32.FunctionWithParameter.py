#Function With Parameter
def greet_user(name):
    print(f'Hi {name}!')
    print("Welcome Aboard")

print("Start")
greet_user("Yash N Sanghavi")
greet_user("John Smit")
print("finished...")

#Function With Positional Parameter
def fullname(first_name,last_name):
    print(f'Welcome Mr.{last_name}')
    print(f'Hey {first_name}')
    print('Welcome To India')

print("Start")
fullname('Yash','Sanghavi')

#Function With Keyword Argument
fullname(last_name="Sanghavi",first_name="MANAN")
