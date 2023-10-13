# warrior class constructor (parent)
class Warrior:
    def __init__(self, name, health, power):
        self.name = name
        self.health = health
        self.power = power

    # alive - to check if warrior is alive, an instance method
    def alive(self):
        return self.health > 0
    
# hero class constructor (child of warrior)
class Hero(Warrior):
    def __init__(self, name, health, power, attributes, weapon):
        super().__init__(name, health, power, attributes, weapon)

    # hero greet
    def greet(self):
        print(f"I am {self.name}, a hero")

    # hero announce
    def announce(self):
        print(f"Listen as I announce myself - {self.name}")

    # hero attack
    def attack(self):
        print(f"{self} executes an attack")

# villain class constructor (child of warrior)
class Villain(Warrior):
    def __init__(self, name, health, power, attributes, weapon):
        super().__init__(name, health, power, attributes, weapon)

    # villain greet
    def greet(self):
        print(f"I offer you a greeting.  I am {self.name}, a villain.")

    # villain annoucne
    def announce(self):
        print(f"I announce myself to you in a villainous manner.  {self.name}")

    # villain attack
    def attack(self):
        print(f"{self.name} plays dirty and executes an attack")



# select a hero
def hero_select():
    thor = Hero("Thor", 30, 15, "Asgardian God of Thudner", "Mjolnir")
    sam = Hero("Sam", "Master of Python", 35, 5, "MacBook Pro")
    frodo = Hero("Frodo Baggins", "Ring-bearer", 60, 35, "The One Ring")
    print()
    print("Select a hero")
    print("1. Thor")
    print("2. Sam")
    print("3. Frodo Baggins")
    print("> ",)
    user_input = input()
    if user_input == "1":
        print("Your hero is Thor")
    elif user_input == "2":
        print("Your hero is Sam")
    elif user_input == "3":
        print("Your hero is Frodo Baggins")
    else:
        print()
        print("Invalid input %r" % user_input)

# select a villain
def villain_select():
    javascript = Villain("JavaScript", 30, 10, "complicated", "Document Object Model")
    zombie = Villain("The Mysterious Undead", float('inf'), 2, None, None)
    vader = Villain("Darth Vader", 60, 25, "Sith Lord", "Force Choke")
    print()
    print("Select a villain")
    print("1. JavaScript")
    print("2. The Mysterious Undead")
    print("3. Darth Vader")
    print("> ",)
    user_input = input()
    if user_input == "1":
        print("Your villain is JavaScript")
    elif user_input == "2":
        print("Your villain is The Mysterious Undead")
    elif user_input == "3":
        print("Your villain is Darth Vader")
    else:
        print()
        print("Invalid input %r" % user_input)

hero_select()
villain_select()