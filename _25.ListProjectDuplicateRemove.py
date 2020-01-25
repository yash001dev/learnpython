#Remove Duplicate Value From Collections.

numbers=[2,2,4,6,3,4,6,1]
unique=[]
for number in numbers:
    if number not in unique:
        unique.append(number)
print(unique)
