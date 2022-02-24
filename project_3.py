"""
Project 1: Poker
Student: Justin
"""

# FUNCTIONS TO CHECK HANDS

# Royal Flush
from random import shuffle
def RoyalFlush(hand):
    if not hand:
        return 0

    valueList = []
    suitList = []
    for card in hand:
        valueList.append(card.value)
        suitList.append(card.suit)

    valueList.sort()

    straightList = list(range(min(valueList), max(valueList)+1))

    if valueList == straightList and len(set(suitList)) == 1 and max(valueList) == 14:
        return 10
    return 0

# Straight Flush
def StraightFlush(hand):
    if not hand:
        return 0

    valueList = []
    suitList = []
    for card in hand:
        valueList.append(card.value)
        suitList.append(card.suit)

    valueList.sort()

    straightList = list(range(min(valueList), max(valueList)+1))

    if valueList == straightList and len(set(suitList)) == 1:
        return 9 + max(valueList)/100
    return 0

# Four of a Kind
def FourOfAKind(hand):
    if not hand:
        return 0

    valueList = []
    for card in hand:
        valueList.append(card.value)

    valueSet = set(valueList)

    if len(valueSet) != 2:
        return 0

    for num in valueSet:
        if valueList.count(num) == 4:
            return 8 + num/100

    return 0

# Full House
def FullHouse(hand):
    if not hand:
        return 0

    valueList = []
    for card in hand:
        valueList.append(card.value)

    valueSet = set(valueList)

    if len(valueSet) != 2:
        return 0

    for num in valueSet:
        if valueList.count(num) == 3:
            return 7 + num/100

    return 0

# Flush
def Flush(hand):
    if not hand:
        return 0

    valueList = []
    suitList = []
    for card in hand:
        valueList.append(card.value)
        suitList.append(card.suit)

    if len(set(suitList)) == 1:
        return 6 + max(valueList)/100
    return 0

# Straight
def Straight(hand):
    if not hand:
        return 0

    valueList = []
    for card in hand:
        valueList.append(card.value)

    valueList.sort()

    straightList = list(range(min(valueList), max(valueList)+1))

    if valueList == straightList:
        return 5 + max(valueList)/100
    return 0

# Three of a Kind
def ThreeOfAKind(hand):
    if not hand:
        return 0

    valueList = []
    for card in hand:
        valueList.append(card.value)

    valueSet = set(valueList)

    if len(valueSet) != 3:
        return 0

    for num in valueSet:
        if valueList.count(num) == 3:
            return 4 + num/100

    return 0

# Two Pairs
def TwoPairs(hand):
    if not hand:
        return 0

    valueList = []
    for card in hand:
        valueList.append(card.value)

    valueSet = set(valueList)

    pairs = [v for v in valueSet if valueList.count(v) == 2]

    if len(pairs) != 2:
        return 0

    for pair in pairs:
        return 3 + pairs[-1]/100

    return 0

# One Pair
def OnePair(hand):
    if not hand:
        return 0

    valueList = []
    for card in hand:
        valueList.append(card.value)

    valueSet = set(valueList)

    pairs = [v for v in valueSet if valueList.count(v) == 2]

    if len(pairs) != 1:
        return 0

    for pair in pairs:
        return 2 + pairs[-1]/100

    return 0

# High Card
def HighCard(hand):
    if not hand:
        return 0

    valueList = []
    for card in hand:
        valueList.append(card.value)

    valueSet = set(valueList)

    if len(valueSet) != 5:
        return 0
    else:
        return 1 + max(valueList)/100


# CARD CLASS
class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __str__(self):
        cardDict = {2: ' 2', 3: ' 3', 4: ' 4', 5: ' 5', 6: ' 6', 7: ' 7', 8: ' 8', 9: ' 9',
                    10: '10', 11: ' J', 12: ' Q', 13: ' K', 14: ' A'}
        return f'{cardDict[self.value]} of {self.suit}'


# DECK CLASS
class Deck:
    def __init__(self):
        self.cards = []
        self.build()
        shuffle(self.cards)

    def build(self):
        for suit in ['\u2663', '\u2660', '\u2666', '\u2665']:
            for value in range(2, 15):
                self.cards.append(Card(suit, value))

    def show(self):
        for card in self.cards:
            print(card)

# PLAYER CLASS
class Player:
    def __init__(self, name, hand=[], money=100):
        self.name = name
        self.hand = hand
        self.score = self.getScore()
        self.money = money
        self.bet = 0

    def getScore(self):
        scores = [RoyalFlush(self.hand), StraightFlush(self.hand), FourOfAKind(self.hand), FullHouse(self.hand),
                  Flush(self.hand), Straight(self.hand), ThreeOfAKind(
                      self.hand), TwoPairs(self.hand),
                  OnePair(self.hand), HighCard(self.hand)]
        self.score = max(scores)
        return self.score

    def sortHand(self):
        self.hand = sorted(self.hand, key=lambda x: x.value, reverse=True)

    def changeCards(self, replacementCards):
        for i in replacementCards.keys():
            self.hand[i] = replacementCards[i]
        self.sortHand()

    def showHand(self):
        self.sortHand()
        for i, card in enumerate(self.hand):
            print('Card ' + str(i+1) + ' - ', end='')
            print(card)

# GAME CLASS
class Game:
    def __init__(self, deck=None, players=[], pot=0):
        self.players = players
        self.deck = Deck()
        self.pot = pot

    def shuffle(self):
        newDeck = Deck()
        self.deck = newDeck

    def dealHand(self):
        for player in self.players:
            hand = []
            for _ in range(5):
                hand.append(self.deck.cards.pop())
            hand = sorted(hand, key=lambda card: card.value, reverse=True)
            player.hand = hand

    def getPlayers(self):
        while True:
            try:
                numberOfPlayers = int(
                    input('Enter number of players (minimum 2 players, maximum 5 players): '))
                print('\n')
                if numberOfPlayers < 2 or numberOfPlayers > 5:
                    continue
                else:
                    break
            except Exception:
                print('Please enter a number between 2 and 5.')

        for num in range(numberOfPlayers):
            name = input("Enter player {}'s name: ".format(num+1))
            print('\n')
            self.players.append(Player(name))

    def printExplanation(self):
        explanation = """
        This is a game of five card poker with single deck.  At the beginning of the game, each
        player will be dealt five cards.  Each player will have an opportunity to review his or
        her hand and decide which cards he or she wants to change out.  The game host will then
        determine who the winner is based on each player's hand.  The winning patterns in order
        of strength are:
        
        Royal Flush
        Straight Flush
        Four of a Kind
        Full House
        Flush
        Straight
        Three of a Kind
        Two Pairs
        One Pair
        High Card
        """

        print('\n')
        print('***** GAME EXPLANATION *****')
        print(explanation)
        print('****************************')
        print('\n')

        while True:
            text = input('Type "--resume" to go back to the game')
            if text == '--resume':
                break

    def changeHands(self):
        for player in self.players:
            while True:
                print("{}, select cards to be replaced, i.e., enter '245' to replace card 2, 4, and 5.".format(
                    player.name))
                print("Leave it blank if you don't need to replace any cards.")
                replaceCardIndices = input('Select cards to be replaced: ')
                print('\n')

                if replaceCardIndices == '--help':
                    self.printExplanation()
                else:
                    try:
                        replaceCardIndices = list(replaceCardIndices)
                        replaceCardIndices = [int(item) for item in replaceCardIndices]

                        if max(replaceCardIndices) <= 5 and min(replaceCardIndices) >= 1:
                            replaceCards = {}
                            for index in replaceCardIndices:
                                replaceCards[index-1] = self.deck.cards.pop()
                            player.changeCards(replaceCards)
                            break
                        else:
                            print('Please enter valid card numbers!')
                    except Exception:
                        print('Please enter numbers only!')

    def showHands(self):
        for player in self.players:
            print('{}, your hand is:'.format(player.name))
            player.showHand()
            print('\n')

    def getWinner(self):
        winner = self.players[0]
        for player in self.players:
            player.getScore()
            if winner.score < player.score:
                winner = player

        print('The winner is {}.'.format(winner.name))
        print('\n')

###### MAIN PROGRAM ######
def main():
    print('POKER GAME')
    game = Game()
    game.getPlayers()

    while True:
        game.dealHand()
        game.showHands()
        game.changeHands()
        game.showHands()
        game.getWinner()

        answer = input('One more round? [y/n]: ')
        while answer not in ['y', 'n']:
            print('Please type "y" for yes or "n" for no.')
            answer = input('One more round? [y/n]: ')
            print('\n')

        if answer == 'n':
            print('Thanks for playing!')
            break
        else:
            game.shuffle()

if __name__ == "__main__":
    main()