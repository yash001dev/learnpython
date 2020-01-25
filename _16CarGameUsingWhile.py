#Game
command=""
started=False
while True:
    command=input("> ").lower()
    if command=="start":
        if started:
            print("Car Already Started...")
        else:
            print("Car Started...")
            started=True
    elif command=="stop":
        print("Car Stoped...")
    elif  command=="help":
        print("""
start-To Start the Car
stop-To Stop the Car
quit-To Quit from Game.
        """)
    elif  command=="quit":
        print("Game is Closed...")
        break
    else:
        print("Sorry I didn't Recognized Your Language.")
    


