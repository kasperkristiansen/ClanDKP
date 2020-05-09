# Imports
import pandas as pd
import csv


# Members list
all_members = [
    "Heimdallr",
    "Marius",
    "Lars"
    ]

all_members1 = [
    "Heimdallr",
    "Marius",
    "Lars",
    "Gulbr",
    "nicnil",
    "Thomas",
    "Bennern96",
    "Marius 2.0",
    "Mannen",
    "ComanderDuche",
    "Norge808",
    "Brodden",
    "Gutten",
    "Bjørnen Sover",
    "Marius 3.0",
    "Jøran",
    "uneven",
    "vonloe",
    "Lars#2",
    "Amadeus",
    "Megvel Jr.",
    "Stygging",
    "Tommy"
]


# Member object
class Member():
    def __init__(self, name):
        self.name = name

    def set_attacking_th_difference(self, th=int):
        """
        th is positive int if th is higher
        th is negative int if th is lower
        """
        self.attacking_th_difference = th

    def set_attack_stars(self, stars=int):
        self.attack_stars = stars

    def set_defending_th_difference(self, th=int):
        """
        th is positive int if th is higher
        th is negative int if th is lower
        """
        self.defending_th_difference = th

    def set_defense_stars(self, stars=int):
        self.defense_stars = stars

    def calc_dkp(self):
        self.dkp = 0

        if self.attack_stars == 3 and self.attacking_th_difference == 0:
            self.dkp += 100
        elif self.attack_stars == 3 and self.attacking_th_difference == 1:
            self.dkp += 100
        elif self.attack_stars == 3 and self.attacking_th_difference == 2:
            self.dkp += 100
        elif self.attack_stars == 3 and self.attacking_th_difference == -1:
            self.dkp += 100
        elif self.attack_stars == 3 and self.attacking_th_difference == -2:
            self.dkp += 100

        elif self.attack_stars == 2 and self.attacking_th_difference == 0:
            self.dkp += 100
        elif self.attack_stars == 2 and self.attacking_th_difference == 1:
            self.dkp += 100
        elif self.attack_stars == 2 and self.attacking_th_difference == 2:
            self.dkp += 100
        elif self.attack_stars == 2 and self.attacking_th_difference == -1:
            self.dkp += 100
        elif self.attack_stars == 2 and self.attacking_th_difference == -2:
            self.dkp += 100

        elif self.attack_stars == 1 and self.attacking_th_difference == 0:
            self.dkp += 100
        elif self.attack_stars == 1 and self.attacking_th_difference == 1:
            self.dkp += 100
        elif self.attack_stars == 1 and self.attacking_th_difference == 2:
            self.dkp += 100
        elif self.attack_stars == 1 and self.attacking_th_difference == -1:
            self.dkp += 100
        elif self.attack_stars == 1 and self.attacking_th_difference == -2:
            self.dkp += 100

        elif self.attack_stars == 0 and self.attacking_th_difference == 0:
            self.dkp += 100
        elif self.attack_stars == 0 and self.attacking_th_difference == 1:
            self.dkp += 100
        elif self.attack_stars == 0 and self.attacking_th_difference == 2:
            self.dkp += 100
        elif self.attack_stars == 0 and self.attacking_th_difference == -1:
            self.dkp += 100
        elif self.attack_stars == 0 and self.attacking_th_difference == -2:
            self.dkp += 100

        ###
        
        if self.defense_stars == 3 and self.defending_th_difference == 0:
            self.dkp += 100
        elif self.defense_stars == 3 and self.defending_th_difference == 1:
            self.dkp += 100
        elif self.defense_stars == 3 and self.defending_th_difference == 2:
            self.dkp += 100
        elif self.defense_stars == 3 and self.defending_th_difference == -1:
            self.dkp += 100
        elif self.defense_stars == 3 and self.defending_th_difference == -2:
            self.dkp += 100

        elif self.defense_stars == 2 and self.defending_th_difference == 0:
            self.dkp += 100
        elif self.defense_stars == 2 and self.defending_th_difference == 1:
            self.dkp += 100
        elif self.defense_stars == 2 and self.defending_th_difference == 2:
            self.dkp += 100
        elif self.defense_stars == 2 and self.defending_th_difference == -1:
            self.dkp += 100
        elif self.defense_stars == 2 and self.defending_th_difference == -2:
            self.dkp += 100

        elif self.defense_stars == 1 and self.defending_th_difference == 0:
            self.dkp += 100
        elif self.defense_stars == 1 and self.defending_th_difference == 1:
            self.dkp += 100
        elif self.defense_stars == 1 and self.defending_th_difference == 2:
            self.dkp += 100
        elif self.defense_stars == 1 and self.defending_th_difference == -1:
            self.dkp += 100
        elif self.defense_stars == 1 and self.defending_th_difference == -2:
            self.dkp += 100

        elif self.defense_stars == 0 and self.defending_th_difference == 0:
            self.dkp += 100
        elif self.defense_stars == 0 and self.defending_th_difference == 1:
            self.dkp += 100
        elif self.defense_stars == 0 and self.defending_th_difference == 2:
            self.dkp += 100
        elif self.defense_stars == 0 and self.defending_th_difference == -1:
            self.dkp += 100
        elif self.defense_stars == 0 and self.defending_th_difference == -2:
            self.dkp += 100



    def make_dict(self):
        self.data = {
            "PlayerName":self.name, 
            "StarsFromAttack":self.attack_stars, 
            "THDiffAttack":self.attacking_th_difference, 
            "StarsDefense":self.defense_stars, 
            "THDiffDefense":self.defending_th_difference,
            "DKP":self.dkp
            }


columns = ["PlayerName","StarsFromAttack","THDiffAttack","StarsDefense","THDiffDefense","DKP"]

file = open("daily_cwl_data.csv", "a", newline="")
writer = csv.DictWriter(file, fieldnames=columns)

for name in all_members:
    player = Member(name)

    print(f"\nCurrent member is {player.name}")

    # Define stars gained from attack
    while True:
        stars = input("Stars from attack: ")

        if stars.isnumeric() == True and int(stars) in [0,1,2,3]:
            player.set_attack_stars(int(stars))
            break
        else:
            print("Input must be a number between 0 and 3\n")


    # Define TH difference on player attack
    while True:
        opponent_th = input(f"Attacking TH difference: ")

        try:
            player.set_attacking_th_difference(int(opponent_th))
            break
        except:
            print("Input must be a positive or negative integer\n")

    
    # Define stars opponent got from attacking base
    while True:
        stars = input("How many stars did the attacker get from your base: ")

        if stars.isnumeric() == True and int(stars) in [0,1,2,3]:
            player.set_defense_stars(int(stars))
            break
        else:
            print("Input must be a number between 0 and 3\n")

    # Define TH difference on player defense
    while True:
        opponent_th = input(f"Defending TH difference: ")

        try:
            player.set_defending_th_difference(int(opponent_th))
            break
        except:
            print("Input must be a positive or negative integer\n")

    player.calc_dkp()
    player.make_dict()

    try:
        writer.writerow(player.data)
        print(f"Writing data: {player.data}")
    except:
        print("Unknown error")

# Close file        
file.close()