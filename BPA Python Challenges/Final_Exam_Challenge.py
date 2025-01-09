import random

name = ""
medical_supplies = random.randint(50, 100)
energy = random.randint(70, 100)
ewoks_treated = 0

def display_status():
    return f"I am {name} and I have {medical_supplies} medical supplies! I'm currently at {energy} energy levels and I've treated {ewoks_treated} ewoks!"

def treat_ewok():
    Minor = Minor
    Moderate = Moderate
    Severe = Severe
    
    print("This ewok's condition is {Condition}.")

    Condition = random.choice(Minor, Moderate, Severe)
    
    if Condition == Minor:
        medical_supplies - 10
        energy + 5
    elif Condition == Moderate:
        medical_supplies - 20
        energy - 0
    else:
        medical_supplies - 30
        energy - 10
print(f"I have {medical_supplies} supplies left and {energy} energy left.")

def start_shift():
    global name

    print("Welcome to the forest moon of Endor!")

    name = input("Enter your name, Medic: ")

    print(f"Welcome, Medic {name}. Ewoks are depending on you.")

    input("Press Enter when ready to begin your shift...")
   
    for _ in range(3):
        encounter_ewok()
        display_status()

        if medical_supplies == 0:
            break
        end_shift()

def encounter_ewok():

    print("An injured Ewok needs your help!")
    while True:
        try:
            Assist = input("Do you want to save this ewok!? Press 1 to save or 2 to skip: ")
            if Assist == 1:
                print("Let's check his status!")
                treat_ewok()
            elif Assist == 2:
                print("oh.. alright then")
            else:
                print("Invalid Response")
        except ValueError as e:
            print(e)

def end_shift():
    print(f"Wonderful Job, you have {medical_supplies} supplies left and your energy is at {energy}!")
    display_status()

start_shift()