class Pet:
    def __init__(self, name):
        self.name = name
        self.hunger = 5     #Default: medium hunger
        self.energy = 5     #Default: medium energy
        self.happiness = 5  #Default: medium happiness
        self.tricks = []    #Empty list to store learned tricks

    def eat(self):
        #Reduces hunger by 3, but not below 0.
        self.hunger = max(self.hunger - 3, 0)   
        #Eating makes the pet happier by 1, but not above 10.
        self.happiness = min(self.happiness + 1, 10)
        print(f"{self.name} is eating 🍖... Yum! Hunger decreased, happiness increased!")

    def sleep(self):
        # Sleep increases energy.
        self.energy = min(self.energy + 5, 10)
        print(f"{self.name} is taking a nap 💤... Energy restored!")

    # By playing, it changes energy, happiness, hunger.
    def play(self):
        self.energy = max(self.energy - 2, 0)  # Takes 2 energy.
        self.happiness = min(self.happiness + 2, 10)  # Increases happiness by 2.
        self.hunger = min(self.hunger + 1, 10)  # Pet becomes a little hungry.
        print(f"{self.name} is playing 🎾! Having fun, but now a bit hungrier and tired.")
    
    # Prints the current status of the pet with labels and emojis.
    def get_status(self):
        print("\n📋 Pet Status:")
        print(f"Name: {self.name}")
        print(f"🍗 Hunger: {self.hunger}/10")
        print(f"⚡ Energy: {self.energy}/10")
        print(f"😊 Happiness: {self.happiness}/10")

    def train(self, trick):
            # Teach a new trick to a pet.
        if trick not in self.tricks:
            #Checks if the trick is already known.
            self.tricks.append(trick)
            print(f"{self.name} learned a new trick: {trick}! 🐾👏")
        else:
            print(f"{self.name} already knows how to {trick}! 😎")
            
    # Prints all the ttricks known by the Pet.
    def show_tricks(self):
        print("\n🎓 Tricks Learned:")
        if self.tricks:
            for i, trick in enumerate(self.tricks, 1):
                print(f"{i}. {trick}")
        else:
            print(f"{self.name} hasn't learned any tricks yet.")

