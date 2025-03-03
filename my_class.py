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
    

    def new_round(self):

        self.hunger = max(0, min(10, self.hunger))              #min(1value, 2value)    if 2value>1value
        self.happiness = max(0, min(10, self.happiness))          #it will return 1value  
        self.health = max(0, min(10, self.health))              #max(1value, 2value) if 2value > 1value
        self.tiredness = max(0, min(10, self.tiredness))           #it will return 2 value 
        self.poop = max(0, min(10, self.poop))   

        self.hunger += randint(0, 2)        
        self.health -= randint(0, 1)         
        self.tiredness += randint(0, 2)      
        self.poop += randint(0, 1)          
        
        self.status()

   



    def status(self):
        print(f"Name: {self.name}")
        print(f"Hunger: {self.hunger}")
        print(f"Happiness: {self.happiness}")
        print(f"Health: {self.health}")
        print(f"Tiredness: {self.tiredness}")
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
        if self.hunger >= 10:
            print("U died of hunger")
            self.alive = False
        elif self.happiness <= 0: 
            print("U died of your mental state")
            self.alive = False
        elif self.health <= 0:  
            print("U died of illness")
            self.alive = False
        elif self.poop >= 10: 
            print("U died of untidines")
            self.alive = False
        elif self.tiredness >= 10:
            print("U died of tiredness")
            self.alive = False
        else:
            self.alive = True 

    def feed(self):
        if self.alive and self.hunger >= 0:
            self.happiness += 2
            self.hunger -= 6
            self.poop += randint(0, 2)
        else:
            print("You died of hunger")
        self.new_round()

    def sleep(self):
        if self.alive and self.tiredness <= 9:
            self.happiness += 2
            self.hunger += 3
            self.tiredness -= 6
        else:
            print("You died of tiredness")
        self.new_round()

    def play(self):
        if self.alive and self.happiness >= 1:
            self.happiness += 5
            self.tiredness += 3
            self.hunger += 3
        else:
            print("You died of boredom")
        self.new_round()

    def clean(self):
        if self.alive and self.poop <= 9:
            self.poop = 0
        else:
            print("Too dirty, you die")
        self.new_round()

    def heal(self):
        if self.alive and self.health >= 1:
            self.health = 10
        else:
            print("You died of illness")
        self.new_round()


myPet = Tamagochi("Amigo")

while True:
    action = input("Enter an action:").strip().lower()
    myPet.perform_action(action)
   
    if myPet.alive = False:
        break
 
   

        



