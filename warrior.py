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
        super().__init__(name, health, power)
        self.attributes = attributes
        self.weapon = weapon

    # hero greet
    def greet(self):
        print(f"\nI am {self.name}, a hero")

    # hero announce
    def announce(self):
        print(f"\nMy heroics know no bounds.  Villains fear me, other heroes wanna be me. - {self.name}")

    # hero attack
    def attack(self):
        print(f"\n{self} executes an attack")

# villain class constructor (child of warrior)
class Villain(Warrior):
    def __init__(self, name, health, power, attributes, weapon):
        super().__init__(name, health, power)
        self.attributes = attributes
        self.weapon = weapon

    # villain greet
    def greet(self):
        print(f"\nI offer you a greeting.  I am {self.name}, a villain.")

    # villain annoucne
    def announce(self):
        print(f"\nI shall corrupt the world!  Noone shall stop me! - {self.name}")

    # villain attack
    def attack(self):
        print(f"\n{self.name} plays dirty and executes an attack")

# instances of hero class
thor = Hero("Thor", 30, 15, "Asgardian God of Thudner", "Mjolnir")
sam = Hero("Sam", "Master of Python", 35, 5, "MacBook Pro")
frodo = Hero("Frodo Baggins", "Ring-bearer", 60, 35, "The One Ring")

# instances of villain class
javascript = Villain("JavaScript", 30, 10, "complicated", "Document Object Model")
zombie = Villain("The Mysterious Undead", float('inf'), 2, None, None)
vader = Villain("Darth Vader", 60, 25, "Sith Lord", "Force Choke")

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
        myhero = thor
    elif user_input == "2":
        myhero = sam
    elif user_input == "3":
        myhero = frodo
    else:
        print("\nInvalid input %r" % user_input)
    myhero.greet()
    myhero.announce()
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
        myvillain = javascript
    elif user_input == "2":
        myvillain = zombie
    elif user_input == "3":
        myvillain = vader
    else:
        print("\nInvalid input %r" % user_input)
    myvillain.greet()
    myvillain.announce()
    return myvillain

hero_select()

villain_select()




