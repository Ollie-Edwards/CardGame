from cards import Deck, Card
from shuffler import Shuffler
from itertools import combinations

gameDeck = Deck()
gameDeck.reset()
gameDeck.cards = Shuffler.fisher_yates_shuffle(gameDeck.cards)

tableCards = Deck()


def getPossibleMoves(board):
    """
    A pair of cards whose values sum to 11
    Trio of face cards
    """
    possibleMoves = []

    numToIndex = {}
    # Use 2Sum to find all pairs which sum to 11
    for i, card in enumerate(board):
        complement = 11 - card.get_value()

        if complement in numToIndex:
            for j in numToIndex[complement]:
                possibleMoves.append([j, i])

        if card.get_value() in numToIndex:
            numToIndex[card.get_value()].append(i)
        else:
            numToIndex[card.get_value()] = [i]

    # Check for trios of face cards
    face_cards = [idx for idx, card in enumerate(board) if card.rank in ["J", "Q", "K"]]
    for trio in combinations(face_cards, 3):
        possibleMoves.append(list(trio))  # or list(trio) if you prefer

    return possibleMoves


def getUserInput():
    while True:
        move = input("Enter Pair or Trio of cards: ")

        try:
            move = [int(i) for i in move.replace(" ", "").split(",")]

            if len(move) not in [2,3]:
                print("You must enter 2 or 3 indexes")
                continue

            if len(move) != len(set(move)):
                print("Duplicate indexes are not allowed.")
                continue

            if move not in getPossibleMoves(tableCards.cards):
                print("Invalid Move")

            return move

        except:
            print("Invalid Move")
            continue

while (
    tableCards.size() < 8 or getPossibleMoves(tableCards.cards) == []
) and gameDeck.size() > 0:
    tableCards.add_card(gameDeck.draw_card())

while True:
    # Debug: Display possible moves
    print(getPossibleMoves(tableCards.cards))

    # Check for win or loss
    if tableCards.cards == []:
        print("You Win!")
        break

    elif getPossibleMoves(tableCards.cards) == 0:
        print("You Loose")
        break

    # Display cards on the table
    for i, card in enumerate(tableCards.cards):
        print(i, ": ", card.get_card_name())

    move = getUserInput()

    # Remove selected cards
    faceUp = [card for idx, card in enumerate(tableCards.cards) if idx not in move]

    while (
        tableCards.size() < 8 or getPossibleMoves(tableCards.cards) == []
    ) and gameDeck.size() > 0:
        tableCards.add_card(gameDeck.draw_card())
