import random 
user = ""
while user != "q":
    options = ("rock", "paper", "scissors")
    CPU = random.choice(options)
    user = input("Choose rock, paper or scissors: ").lower()
                                            #           scissors
    while user != "rock" and user != "paper" and user != "scissors":
        user = input("Choose rock, paper or scissors (q to quit): ").lower()

    if CPU == user:
        print(f"CPU chose {CPU},  Tie!")
    elif CPU == "rock":
        
        if user == "scissors":
            print(f"CPU chose {CPU},  you lost!")
        elif user == "paper":
            print(f"CPU chose {CPU},  you won!")
    elif CPU == "scissors":
        if user == "rock":
            print(f"CPU chose {CPU},  you won!")
        elif user == "paper":
            print(f"CPU chose {CPU},  you lost!")
    elif CPU == "paper":
        if user == "rock":
            print(f"CPU chose {CPU},  you lost!")
        elif user == "scissors":
            print(f"CPU chose {CPU},  you won!")



