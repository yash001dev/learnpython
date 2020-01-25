weight=input("Enter Weight:")
unit=input('(L)bs or (K)g:')
if unit.upper()=="L":
    converter=float(weight)*0.45
    print(f"You are {converter} Kilos")
else:
    converter=float(weight)/0.45
    print(f"You are {converter} Pounds")

    