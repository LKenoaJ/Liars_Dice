from player import Player, CPU
from bidding import *
class Table:
    def __init__(self):
        #self.totalDice = self.collectDice()
        self.tableHand = []
        self.players = self.getPlayers()
        self.playerCount = self.getPlayerCount()
        self.initialBid = {'quantity': 0, 'value': 0}
        self.tableBid = self.initialBid

    def getPlayers(self):
        while True:
            try:
                playerCount = int(input("Enter Player Count (1-8):\n"))
                if 1 <= playerCount <= 8:
                    break
                print("Invalid input. Enter a number between 1 and 8.\n")
            except ValueError:
                print("Invalid input. Enter a valid number.\n")
        players = [Player()]  # Human player
        for _ in range(playerCount - 1):
            players.append(CPU())  # CPU players
        return players
    
    def getPlayerCount(self):
        playercount = 0
        for player in self.players:
            playercount += 1
        return playercount

    def rollTable(self):
        for player in self.players:
            player.rollHand()

    def updateTotalDice(self):
        # Update the total number of dice left on the table after each round
        self.totalDice = sum(len(player.hand) for player in self.players if len(player.hand) > 0)
        print(f"Total dice remaining on the table: {self.totalDice}")

    def getTableHand(self):
        tempHand = []
        print(f"Revealing all dice on the table...")
        for player in self.players:
            tempHand.append(player.hand)
            print(f"{player.name} rolled {player.hand}")
        self.tableHand = tempHand



    def startGame(self):
        while True:
            round = 0
            self.startRound(round)
            checkHands(self)
            for player in self.players:
                print(player.name)
            print("New Round")
            #Play 1 Round (UNtil 1 die is knocked out)
    #Each round loops turns until an a bid is correctly called or an incorrect call is made. 
    #Then the round ends and the loser has one die removed from their hand 

    def startRound(self, round):
        self.rollTable()
        self.tableBid = self.initialBid
        self.startTurn(self.initialBid, self.tableBid)
        round += 1

    def startTurn(self, initialBid, tableBid):
        turn = 0  # Tracks the overall turn count
        currentPlayerIndex = 0  # Tracks the index of the current player

        while True:  # Loop until the round ends
            currentPlayer = self.players[currentPlayerIndex]
            previousPlayer = self.players[(currentPlayerIndex - 1) % len(self.players)]  # Correctly references the last player

            print(f"Turn: {turn}, Current Player: {currentPlayer.name}, Previous Player: {previousPlayer.name}")

            # First player's first turn of the round - They must bid
            if turn == 0 and currentPlayerIndex == 0:
                print("It is the first turn of the round, the first player (You) must bid.")
                tableBid = currentPlayer.makeBid(tableBid)
                turn += 1  # Increment turn after a bid
                currentPlayerIndex = (currentPlayerIndex + 1) % len(self.players)  # Move to the next player
                continue

            # Human player's turn
            elif currentPlayerIndex == 0:  # Human player logic
                while True:
                    call = input(f'''The last bid was {tableBid['quantity']} lots of {tableBid['value']}.
                                Do you wish to call? (Yes/No)''').strip().lower()
                    if call == "yes":
                        callLastBid(self, currentPlayer, previousPlayer)  # Resolve call
                        return  # End the round after resolving a call
                    elif call == "no":
                        tableBid = currentPlayer.makeBid(tableBid)
                        turn += 1  # Increment turn after a bid
                        currentPlayerIndex = (currentPlayerIndex + 1) % len(self.players)  # Move to the next player
                        break  # Exit the input loop to proceed with the game
                    else:
                        print("Invalid input. Please enter 'Yes' or 'No'.")  # Retry on invalid input

            # CPU player's turn
            else:
                print(f"{currentPlayer.name}'s turn.")
                turn += 1  # Increment turn after a bid
                currentPlayerIndex = (currentPlayerIndex + 1) % len(self.players)  


                            
