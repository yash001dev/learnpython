#Make Simple Gussing Programme using While Loop

secreat_number=9
secreat_count=0
while secreat_count<3:
    user_number=int(input("Enter Guess:"))
    if(user_number==secreat_number):
        print("You Won...")
        break
    secreat_count+=1
else:
    print("Sorry You Cannot Guess Correct Number...")
