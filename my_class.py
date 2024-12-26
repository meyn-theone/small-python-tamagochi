from random import randint

class Tamagochi:
    def __init__(self, name):
        self.name = name 
        self.hunger = 0
        self.health = 10
        self.happiness = 10
        self.alive = True
        self.tiredness = 0
        self.poop = 0

        self.actions = {
            "feed": self.feed,
            "sleep": self.sleep,
            "play": self.play,
            "clean": self.clean,
            "heal": self.heal,
        }    
    
    def status(self):
        print(f"Name: {self.name}")
        print(f"Hunger: {self.hunger}")
        print(f"Happiness: {self.happiness}")
        print(f"Health: {self.health}")
        print(f"Tiredness: {self.tiredness}")
        print(f"Alive: {self.alive}")
        print(f"Poops: {self.poop}")
        if self.alive == False:
            print("Your pet is dead, be more patient next time.")   

    def perform_action(self, action_name): 
        action = self.actions.get(action_name)
        if action:
            action()
            self.death()
        else:
            print(f"Invalid action. Please choose from {list(self.actions.keys())}")

    def death(self):
        if self.hunger >= 10 or self.happiness <= 0 or self.health <= 0 or self.poop >= 10 or self.tiredness >= 10:
            self.alive = False

    def feed(self):
        if self.alive and self.hunger >= 1:
            self.happiness += 2
            self.hunger -= 3
            self.poop += randint(0, 2)
        else:
            print("You died of hunger")
        self.status()

    def sleep(self):
        if self.alive and self.tiredness <= 9:
            self.happiness += 2
            self.hunger += 3
            self.tiredness -= 6
        else:
            print("You died of tiredness")
        self.status()

    def play(self):
        if self.alive and self.happiness >= 1:
            self.happiness += 5
            self.tiredness += 3
        else:
            print("You died of boredom")
        self.status()

    def clean(self):
        if self.alive and self.poop <= 9:
            self.poop = 0
        else:
            print("Too dirty, you die")
        self.status()

    def heal(self):
        if self.alive and self.health >= 1:
            self.health = 10
        else:
            print("You died of illness")
        self.status()

    def new_round(self):
        self.hunger += randint(0, 2) 
        self.health -= randint(0, 1)
        self.tiredness -= randint(0, 2)
        self.hunger = min(self.hunger, 10)
        self.health = max(0, self.health)
        self.happiness = max(0, self.happiness)
        self.tiredness = max(0, self.tiredness)

myPet = Tamagochi("Amigo")

while True:
    if not myPet.alive:
        break
    action = input("Enter an action: ").strip().lower()
    myPet.perform_action(action)
    myPet.new_round()

   
   

        



