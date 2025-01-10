#Kaleb Bogart
import random

name = ""
weapon = ""
health = random.randint(7,10) * 5
gold = 0
strength = random.randint(12,17)
level = 1

def display_character():
    return f"Your currrent weapon is a {weapon}, you have {health} health points. You currently have {gold} gold, your strength level is {strength}. You're level {level}."

def start_encounter():
    Fight = input("You have entered a fight! Would you like to attack (1) or retreat (2): ")
    if Fight == 1:
        start_fight()
    elif Fight == 2:
        print("You have ran away! Be careful next time...")
    else:
        print("Invalid Response!")

def start_fight():
    Easy = Easy
    Hard = Hard
    display_character()
    Enemy = random.choice(Easy, Hard)
    if Enemy == Easy:
        print("This Enemy is easy, you will take 5 damage, gain 3 gold, and upgrade by 1 level!")
        gold + 3
        health - 5
        level + 1
    elif Enemy == Hard:
        print("This enemy is difficult, you will lose 10 health, gain 10 gold, and upgrade by 2 levels!")
        gold + 10
        health - 10
        level + 2
    

def start_game():
    print("Welcome to the dungeon!")
    print("You will fight 3 enemies of varying difficulty! If you're able to survive, you will receive Treasure!")
    name = input("What is your name, adventurer? ")
    weapon = input("What is your weapon of choice? ")
    print(f"Ahh yes {name}, I see you have brought your {weapon} with you! Good, you will need it!")
    for _ in range(3):
        display_character()
        start_encounter()
        if health == 0:
            break
        end_game

def end_game():
    if health == 0:
        print("You've done well soldier, the corp is proud of you! Maybe the treasure will be found another day...")
    else:
        print("Congrats Soldier! You have found the treasure and will live a wealthy life!")

start_game()