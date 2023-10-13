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
        # super().__init__(name, health, power, attributes, weapon)
        self.attributes = attributes
        self.weapon = weapon

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
        # super().__init__(name, health, power, attributes, weapon)
        self.attributes = attributes
        self.weapon = weapon

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
    print()
    print("Select a hero")
    print("1. Thor")
    print("2. Sam")
    print("3. Frodo Baggins")
    print("> ",)
    user_input = input()
    if user_input == "1":
        # print("Your hero is Thor")
        thor = Hero("Thor", 30, 15, "Asgardian God of Thudner", "Mjolnir")
        myhero = thor
        greet(myhero)
    elif user_input == "2":
        # print("Your hero is Sam")
        sam = Hero("Sam", "Master of Python", 35, 5, "MacBook Pro")
        myhero = sam
    elif user_input == "3":
        # print("Your hero is Frodo Baggins")
        frodo = Hero("Frodo Baggins", "Ring-bearer", 60, 35, "The One Ring")
        myhero = frodo
    else:
        print()
        print("Invalid input %r" % user_input)
    return myhero

# select a villain
def villain_select():
    print()
    print("Select a villain")
    print("1. JavaScript")
    print("2. The Mysterious Undead")
    print("3. Darth Vader")
    print("> ",)
    user_input = input()
    if user_input == "1":
        # print("Your villain is JavaScript")
        javascript = Villain("JavaScript", 30, 10, "complicated", "Document Object Model")
        myvillain = javascript
    elif user_input == "2":
        # print("Your villain is The Mysterious Undead")
        zombie = Villain("The Mysterious Undead", float('inf'), 2, None, None)
        myvillain = zombie
    elif user_input == "3":
        # print("Your villain is Darth Vader")
        vader = Villain("Darth Vader", 60, 25, "Sith Lord", "Force Choke")
        myvillain = vader
    else:
        print()
        print("Invalid input %r" % user_input)
    return myvillain

hero_select()
villain_select()