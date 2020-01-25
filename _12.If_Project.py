name=input("Enter Your Name:")

if len(name)<3:
    print("Name at least 3 characters...")
elif len(name)>50:
    print("Name must be a maximum chracters...")
else:
    print("Your Name Looks Good...")
    