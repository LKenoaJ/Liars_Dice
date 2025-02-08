import random

class Player:
    def __init__ (self):
        self.score = 0
        self.name = self.getName()
        self.hand = []
        self.handsize = 7

    def getName(self):
        while True:
            name = input("Enter the player's name (max 15 characters, no special characters):\n")
            if len(name) <= 15 and all(char.isalnum() for char in name):
                return name
            print("Invalid name. Try again.\n")


    def rollHand(self):
        self.hand = []
        for _ in range(self.handsize):
            self.hand.append(random.randint(1,6))


    def makeBid(self, tableBid):
        validBid = False    
        currentBid = {'quantity': 0, 'value': 0}
        while True:
            try:
                currentBid['quantity'] = int(input("Enter the bid quantity: "))
                currentBid['value'] = int(input("Enter the bid die face value: "))
            except ValueError:
                print("Error, Invalid Input Type, retry.")
            validBid = self.checkBid(currentBid, tableBid)
            if validBid == True:
                print(f"{self.name} has bid {currentBid['quantity']} dice showing {currentBid['value']}.")
                return currentBid
            print(f"""Invalid Bid, ensure the correct values have been entered.
            The quantity of dice entered must be higher than: {currentBid['quantity']}
            Unless the face value is higher than {currentBid['value']}, in which case it can be equal, BUT NOT LOWER.
            The die face value must be between 1 and 6.""")

 
    def checkBid(self, currentBid, tableBid):
        if not (1 <= currentBid['value'] <= 6):
            print(f"Invalid die face value: {currentBid['value']}. It must be between 1 and 6.")
            return False
        if currentBid['quantity'] < tableBid['quantity'] or \
        (currentBid['quantity'] == tableBid['quantity'] and currentBid['value'] <= tableBid['value']):
            return False
        
        return True

class CPU(Player):
    def __init__(self):
        # Directly initialize attributes without calling `super().__init__()`
        self.score = 0
        self.name = self.getCPUName()  # Set a random name for the CPU
        self.hand = []
        self.handsize = 7

    def getCPUName(self):
        name_list = [
            "Akamu", "Akiliano", "Akoni", "Hale", "Hau'oli", "Hiapo", 
            "Ka Hiwa", "Kai", "Kalani", "Kaulana", "Kekoa", "Kealoha", 
            "Keone", "Koa", "Maka", "Mana", "Mano", "Mililani", 
            "Nana", "Niele", "Noa", "Noe", "Palani", "Pilialoha", "Punahele"
        ]
        return random.choice(name_list)