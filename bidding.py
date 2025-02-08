#---------- All Bidding Mechanics
def callLastBid(self, currentPlayer, previousPlayer):
    print(f"{currentPlayer.name} has called the last bid!")
    self.getTableHand()
    call = checkBid(self, self.tableBid, currentPlayer, previousPlayer )
    print(f'current {currentPlayer.name}\n prev {previousPlayer.name}')
    roundConsequence(call, currentPlayer, previousPlayer)

def checkBid(self, tableBid, currentPlayer, previousPlayer):
    #Collect the quantity of the Face Value called
    faceValue = tableBid['value']
    faceCount = 0
    for die in self.tableHand:
        if die == faceValue:
            faceCount += 1
    if tableBid['quantity'] < faceCount:
        return False
    return True
    
def roundConsequence(call, currentPlayer, previousPlayer):
    print(f'currentplayer = {currentPlayer.name}\n prevplayer = {previousPlayer.name}')
    if call == True:
        #remove die from previous player
        print(f'{currentPlayer.name} has called your bluff!\n{previousPlayer.name}, you lose one die!')
        previousPlayer.hand.pop()
        previousPlayer.handsize -= 1
        print(f'{previousPlayer.name} now has {previousPlayer.handsize} dice remaining.')
    else:
        print(f'''{currentPlayer.name} has called incorrectly called {previousPlayer.name} a Liar!\n
                {currentPlayer.name}, you lose a die!''')
        currentPlayer.hand.pop()
        currentPlayer.handsize -= 1
        print(f'{currentPlayer.name} now has {currentPlayer.handsize} dice remaining.')


def checkHands(self):
    for player in self.players[:]:  # copy list
        if player.handsize == 0:
            print(f'{player.name} has lost.')
            self.players.remove(player)
    return self.players

