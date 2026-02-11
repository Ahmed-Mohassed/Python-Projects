import json
import random
import os
#Future improvements
# add colors using colorama or whatever
# GUI
# Difficulties
# Fix the List bugs (not english charecters)#
Capitals = {}
base_dir = os.path.dirname(os.path.abspath(__file__))
filepath = os.path.join(base_dir, "Capitals.json")
if os.path.exists(filepath):

    with open(filepath, "r") as file:
        Capitals = json.load(file)

    Capitals_num = len(Capitals)
    while True:
        try:
            Qnum = int(input("Enter the number of questions you want: "))
            if Qnum <= Capitals_num and Qnum > 0:
                break

            else:
                print(f"The number should be less than {Capitals_num} and more than 1!")
        except ValueError:
            print("Enter a valid number")

    Countries = []
    while len(Countries) != Qnum:
        item  = random.choice(list(Capitals.keys()))
        if item not in Countries:
            Countries.append(item)

    score = 0

    def get_options(Country):
        Capital = Capitals.get(Country)
        option_list = [Capital]
        while len(option_list)!= 4:
            op = random.choice(list(Capitals.values()))
            if op not in option_list:
                option_list.append(op)
        random.shuffle(option_list)
        option_list.append(option_list.index(Capital)+1)
        return option_list #Returns Index of the correct answer at the end

    for item in Countries:
        options = get_options(item)
        print(f"What is the capital of {item}?")
        print(f"A.{options[0]}")
        print(f"B.{options[1]}")
        print(f"C.{options[2]}")
        print(f"D.{options[3]}")
        while True:
            chosen = input("(A/B/C/D): ").upper()
            if chosen == "A" or chosen == "B" or chosen == "C" or chosen == "D":
                break
            else:
                print("Enter a valid input (A/B/C/D)")
        match chosen:
            case "A":
                chosen = 1
            case "B":
                chosen = 2
            case "C":
                chosen = 3
            case "D":
                chosen = 4
        if chosen == options[4]:
            score += 1
            print("Correct Answer!")
        else:
            print(f"Incorrect Answer!\nThe Correct answer was {options[options[4]-1]}")
    print(f"Score: {score} / {Qnum}")
    print(f"percentage: {score/Qnum * 100:.1f}%")
else:
    print("File not Found")
