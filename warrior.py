# warrior class constructor (parent)
class Warrior:
    def __init__(self, name, health, power):
        self.name = name
        self.health = health
        self.power = power

    # alive - to check if warrior is alive, an instance method
    def alive(self):
        return self.health > 0
    
   # print status - an instance method
    def print_status(self, other):
        if other.alive():
            print()
            print (f"{self.name} health: {self.health}")
        if self.alive():
            print()
            print (f"{other.name} health: {other.health}")
        else:
            print()
            print(f"{self.name} has died.  The world is now a much darker place.")
            print()
    
# hero class constructor (child of warrior)
class Hero(Warrior):
    def __init__(self, name, health, power, attributes, weapon):
        super().__init__(name, health, power)
        # self.name = name
        # self.health = health
        # self.power = power
        self.attributes = attributes
        self.weapon = weapon

    # hero greet
    def greet(self):
        print(f"\nI am {self.name} the {self.attributes}, a hero of mythical proportions.  ")

    # hero announce
    def announce(self):
        print(f"\nMy heroics know no bounds.  \nVillains fear me, other heroes wanna be me.  \nI wield the power of {self.weapon} and you will feel my fury.  \n- {self.name}")

    # hero attack
    def attack(self, other):
        other.health -= self.power

        if self.alive():
            print(f"\n{self.name} executes an attack, which does %d damage to {myvillain.name}." % self.power)
        else:
            print(f"\n{self.name} has died.  \nGame is over, go home.  \nLife sucks.")

    # hero do nothing
    def nothing(self):
        myvillain.attack(myhero)

    # hero flee
    def flee(self):
        print("test")
        print(f"\n{self.name} has chosen to flee.  \nGood luck in life, coward.  \nYou piece of crap.")
        exit()

# villain class constructor (child of warrior)
class Villain(Warrior):
    def __init__(self, name, health, power, attributes, weapon):
        super().__init__(name, health, power)
        # self.name = name
        # self.health = health
        # self.power = power
        self.attributes = attributes
        self.weapon = weapon

    # villain greet
    def greet(self):
        print(f"\nI offer you a greeting.  \nI am {self.name} the {self.attributes}, a villain.")

    # villain annoucne
    def announce(self):
        print(f"\nI shall corrupt the world!  \nWith the power of my {self.weapon}, noone shall stop me! \n- {self.name}")

    # villain attack
    def attack(self, other):
        other.health -= self.power
        if self.alive():
            print(f"\n{self.name} plays dirty and executes an attack.  \nIt strikes {other.name} and does %d damage." % self.power)

        else:
            print(f"\n{self.name} has died.  \nThe sky opens up to a beautiful blue hue.  \nHope wells up inside of our hero.  \nMaybe everything will be ok after all.")


# instances of hero class
thor = Hero("Thor", 30, 15, "Asgardian God of Thudner", "Mjolnir")
sam = Hero("Sam", 35, 5, "Master of Python", "MacBook Pro")
frodo = Hero("Frodo Baggins", 60, 35, "Ring-bearer", "The One Ring")

# instances of villain class
javascript = Villain("JavaScript", 30, 10, "complicated", "Document Object Model")
zombie = Villain("The Mysterious Undead", float('inf'), 2, None, None)
vader = Villain("Darth Vader", 60, 25, "Sith Lord", "Force Choke")

# select a hero
print("\nSelect a hero")
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


while myhero.alive() and myvillain.alive():
    print("\nWhat do you want to do?")
    print("1. Launch attack")
    print("2. Do nothing")
    print("3. Flee")
    print("> ",)
    user_input = input()
    if user_input == "1" and myhero.alive() and myvillain.alive():
        myhero.attack(myvillain)
        myvillain.attack(myhero)
        myhero.print_status(myvillain)
        # if myvillain.alive():
        #     myvillain.print_status(myhero)
        # if myhero.alive():
        #     myhero.print_status(myvillain)
    elif user_input == "2":
        # myhero.nothing(myvillain)
        myvillain.attack(myhero)
        if myhero.alive():
            myhero.print_status(myvillain)
    elif user_input == "3":
        myhero.flee()
    else:
        print("Invalid input %r" % user_input)