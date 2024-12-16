class Character:
    def __init__(self, name, id_number):
    name = name
    id_number = id_number

def set_name(self, name):
    self.__name = name

def set_id_number(self, id_number):
    self.__id_number = id_number

def get_name(self):
    return self.__name

def get_id_number(self):
    return self.__id_number

class Hero(Character):
    def __init__(self, name, id_number, level, loot):
        Character.__init__(self, name, id_number)

# Initialize the level and loot attributes.

level = level

loot = loot

# Mutator functions for level and loot.

def set_level(self, level):
    self.__level = level

def set_pay_rate(self, __loot):
    self.__loot = loot

# Accessor functions for level and loot.

def get_level(self):
    return self.__level

def get_loot(self):
    return self.__loot

class Boss(Character):
    def __init__(self, name, id_number, level, hp, attack_damage):
        Character .__init__(self, name, id_number)

# Initialize the level, hp, attack damanage, lifespan attributes.

level = level

hp = hp

attack_damage = attack_damage

lifespan = 0

# Mutator functions for level, hp, attack damanage, lifespan.

def set_level(self, level):
    self.__level = level

def set_hp(self, hp):
    self.__hp = hp

def set_attack_damage(self, attack_damage):
    self.__attack_damage = attack_damage

def set_lifespan(self, lifespan):
    self.__lifespan = lifespan

# Accessor functions for level, hp, attack damanage, lifespan

def get_level(self):
    return self.__level

def get_hp(self):
    return self.__hp

def get_attack_damage(self):
    return self.__attack_damage

def get_lifespan(self):
    return (self.__hp / 300)

# Character Information Program
# MemberID

def main():
    hero_name = ''
    hero_id = ''
    hero_shift = 0
    hero_pay = 0.0
    boss_name= ''
    boss_id = ''
    boss_level = 0
    boss_hp = 0.0
    boss_attack_damage = 0.0
    boss_lifespan = 0.0

# Get Hero data attributes

print ('Hero Data Entry:')

hero_name = input('Enter the hero name: ')
hero_id = input('Enter the character ID number: ')
hero_level = int(input('Enter the hero level: '))
hero_loot = float(input('Enter the hero loot value: '))

# Create an instance of Hero

hero = Character.Hero(hero_name, hero_id, hero_level, hero_loot)

# Get Boss data attributes.

print ('')
print ('Boss Data Entry:')
boss_name = input('Enter the boss name: ')
boss_id = input('Enter the character ID number: ')
boss_level = int(input('Enter the boss level: '))
boss_hp = float(input('Enter the boss hp: '))
boss_attack_damage = float(input('Enter the boss attack damage: '))

# Create an instance of Boss.

boss = Character.Boss(boss_name, boss_id, boss_level, boss_hp, boss_attack_damage)

# Display Hero information

print ('')
print ('Hero information:')
print (f'Name: {hero.get_name()}')
print (f'ID number: {hero.get_id_number()}')
print (f'Level: {hero.get_level()}')
print (f'Loot: ${hero.get_loot():,.2f}')

print ('')
print ('Boss information: ')
print (f'Name: {boss.get_name()}')
print (f'ID number: {boss.get_id_number()}')
print (f'Level: {boss.get_level()}')
print (f'HP: {boss.get_hp()}')
print (f'Attack Damage: {boss.get_attack_damage()}')
print (f'Lifespan: {boss.get_lifespan():,.2f} attacks')

# Call the main function.

if __name__ == '__main__':
    main()