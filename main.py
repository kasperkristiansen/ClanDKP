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
        The th difference between this member and the
        person he raided
        th is positive int if th is higher
        th is negative int if th is lower
        """
        self.attacking_th_difference = th

    def set_attack_stars(self, stars=int):
        """
        Define the stars gained from attacking
        """
        self.attack_stars = stars

    def set_defending_th_difference(self, th=int):
        """
        The th difference between this member and the
        person who raided them
        th is positive int if th is higher
        th is negative int if th is lower
        """
        self.defending_th_difference = th

    def set_defense_stars(self, stars=int):
        """
        Define the stars the opponent got from attacking
        this member's base
        """
        self.defense_stars = stars

    def set_got_attacked(self, fact):
        """
        Set if the player got raided or not in current war
        """
        if fact == "y":
            self.got_attacked = True
        elif fact == "n":
            self.got_attacked = False
            self.defense_stars = "NaN"
            self.defending_th_difference = "NaN"

    def set_used_attack(self, fact):
        """
        Set if the player used their attack in the war
        """
        if fact == "y":
            self.used_attack = True
        elif fact == "n":
            self.used_attack = False
            self.attack_stars = "NaN"
            self.attacking_th_difference = "NaN"

    def calc_dkp(self):
        """
        Calculate the DKP score for this clan member
        """
        self.dkp = 0

        if self.attack_stars == 3 and self.attacking_th_difference == 0:
            self.dkp += 3
        elif self.attack_stars == 3 and self.attacking_th_difference == 1:
            self.dkp += 5
        elif self.attack_stars == 3 and self.attacking_th_difference == 2:
            self.dkp += 5
        elif self.attack_stars == 3 and self.attacking_th_difference == -1:
            self.dkp += 1
        elif self.attack_stars == 3 and self.attacking_th_difference == -2:
            self.dkp += 1

        elif self.attack_stars == 2 and self.attacking_th_difference == 0:
            self.dkp += 2
        elif self.attack_stars == 2 and self.attacking_th_difference == 1:
            self.dkp += 4
        elif self.attack_stars == 2 and self.attacking_th_difference == 2:
            self.dkp += 4
        elif self.attack_stars == 2 and self.attacking_th_difference == -1:
            self.dkp += 0
        elif self.attack_stars == 2 and self.attacking_th_difference == -2:
            self.dkp += 0

        elif self.attack_stars == 1 and self.attacking_th_difference == 0:
            self.dkp += 0
        elif self.attack_stars == 1 and self.attacking_th_difference == 1:
            self.dkp += 0
        elif self.attack_stars == 1 and self.attacking_th_difference == 2:
            self.dkp += 0
        elif self.attack_stars == 1 and self.attacking_th_difference == -1:
            self.dkp -= 2
        elif self.attack_stars == 1 and self.attacking_th_difference == -2:
            self.dkp -= 2

        elif self.attack_stars == 0 and self.attacking_th_difference == 0:
            self.dkp -= 1
        elif self.attack_stars == 0 and self.attacking_th_difference == 1:
            self.dkp -= 1
        elif self.attack_stars == 0 and self.attacking_th_difference == 2:
            self.dkp -= 1
        elif self.attack_stars == 0 and self.attacking_th_difference == -1:
            self.dkp -= 5
        elif self.attack_stars == 0 and self.attacking_th_difference == -2:
            self.dkp -= 5

        ###

        if self.got_attacked == True:

            if self.defense_stars == 3 and self.defending_th_difference == 0:
                self.dkp += 0
            elif self.defense_stars == 3 and self.defending_th_difference == 1:
                self.dkp += 0
            elif self.defense_stars == 3 and self.defending_th_difference == 2:
                self.dkp += 0
            elif self.defense_stars == 3 and self.defending_th_difference == -1:
                self.dkp -= 2
            elif self.defense_stars == 3 and self.defending_th_difference == -2:
                self.dkp -= 2

            elif self.defense_stars == 2 and self.defending_th_difference == 0:
                self.dkp += 1
            elif self.defense_stars == 2 and self.defending_th_difference == 1:
                self.dkp += 2
            elif self.defense_stars == 2 and self.defending_th_difference == 2:
                self.dkp += 2
            elif self.defense_stars == 2 and self.defending_th_difference == -1:
                self.dkp -= 1
            elif self.defense_stars == 2 and self.defending_th_difference == -2:
                self.dkp -= 1

            elif self.defense_stars == 1 and self.defending_th_difference == 0:
                self.dkp += 2
            elif self.defense_stars == 1 and self.defending_th_difference == 1:
                self.dkp += 4
            elif self.defense_stars == 1 and self.defending_th_difference == 2:
                self.dkp += 4
            elif self.defense_stars == 1 and self.defending_th_difference == -1:
                self.dkp += 0
            elif self.defense_stars == 1 and self.defending_th_difference == -2:
                self.dkp += 0

            elif self.defense_stars == 0 and self.defending_th_difference == 0:
                self.dkp += 3
            elif self.defense_stars == 0 and self.defending_th_difference == 1:
                self.dkp += 5
            elif self.defense_stars == 0 and self.defending_th_difference == 2:
                self.dkp += 5
            elif self.defense_stars == 0 and self.defending_th_difference == -1:
                self.dkp += 2
            elif self.defense_stars == 0 and self.defending_th_difference == -2:
                self.dkp += 2

    def make_dict(self):
        """
        Creates the dictionary used to write
        to the csv file
        """
        self.data = {
            "PlayerName":self.name, 
            "UsedAttack":self.used_attack,
            "StarsFromAttack":self.attack_stars, 
            "THDiffAttack":self.attacking_th_difference, 
            "GotAttacked":self.got_attacked,
            "StarsDefense":self.defense_stars, 
            "THDiffDefense":self.defending_th_difference,
            "DKP":self.dkp
            }


# Get all column names
with open("daily_cwl_data.csv", "r") as f:
    reader = csv.reader(f)
    columns = next(reader)

# Open file
file = open("daily_cwl_data.csv", "a", newline="")

# Create writer
writer = csv.DictWriter(file, fieldnames=columns)

# For every clan member
for name in all_members:

    # Create player instance
    player = Member(name)
    print(f"\nCurrent member is {player.name}")

    # Get if member was in war or not
    while True:
        in_war = input("Is the member in the war y/n: ")

        if in_war == "y" or in_war == "n":
            break

    # Skip if not in war
    if in_war == "n":
        print(f"Skipping user {player.name}")
    
    else:

        while True:
            used_attack = input("Did the player use their attack (y/n): ")

            if used_attack == "y" or used_attack == "n":
                player.set_used_attack(used_attack)
                break
        
        if player.used_attack == False:
            print(f"Inserting NaN values for attacks")

        else:
            # Define stars gained from attack
            while True:
                stars = input("Stars from attack: ")

                # Ensure input is an int and is a value between 0 and 3
                if stars.isnumeric() == True and int(stars) in [0,1,2,3]:
                    player.set_attack_stars(int(stars))
                    break
                else:
                    print("Input must be a number between 0 and 3\n")


            # Define TH difference on player attack
            while True:
                opponent_th = input(f"Attacking TH difference: ")

                # Ensure input is an int
                try:
                    player.set_attacking_th_difference(int(opponent_th))
                    break
                except:
                    print("Input must be a positive or negative integer\n")


        # Find out if player got raided or not
        while True:
            got_attacked = input("Did member get attacked in war (y/n): ")

            if got_attacked == "y" or got_attacked == "n":
                player.set_got_attacked(got_attacked)
                break

        # Insert NaN values for defense if player didnt get attacked
        if player.got_attacked == False:
            print("Setting NaN values for defense")

        else:
            # Define stars opponent got from attacking base
            while True:
                stars = input("How many stars did the attacker get from your base: ")

                # Ensure input is an int and is a value between 0 and 3
                if stars.isnumeric() == True and int(stars) in [0,1,2,3]:
                    player.set_defense_stars(int(stars))
                    break
                else:
                    print("Input must be a number between 0 and 3\n")

            # Define TH difference on player defense
            while True:
                opponent_th = input(f"Defending TH difference: ")

                # Ensure input is an int
                try:
                    player.set_defending_th_difference(int(opponent_th))
                    break
                except:
                    print("Input must be a positive or negative integer\n")

        # Calculate dkp
        player.calc_dkp()

        # Make dictionary to insert to csv file
        player.make_dict()

        # If the write fails print unknown error
        # Because I literally dont know what error it could be
        try:
            writer.writerow(player.data)
            print(f"Writing data: {player.data}")
        except:
            print("Unknown error")

# Close file        
file.close()