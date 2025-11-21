from cards import Deck, Card
from shuffler import Shuffler
from itertools import combinations
import pygame
import time

CARD_WIDTH = 100
CARD_HEIGHT = 146

selected = []
status = True

gameDeck = Deck()
gameDeck.cards = Shuffler.fisher_yates_shuffle(gameDeck.cards)

tableCards = Deck()
tableCards.cards = []

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
                possibleMoves.append(sorted([j, i]))

        if card.get_value() in numToIndex:
            numToIndex[card.get_value()].append(i)
        else:
            numToIndex[card.get_value()] = [i]

    # Check for trios of face cards
    face_cards = [idx for idx, card in enumerate(board) if card.rank in ["J", "Q", "K"]]
    for trio in combinations(face_cards, 3):
        possibleMoves.append(sorted(list(trio)))  # or list(trio) if you prefer

    return possibleMoves


def getUserInput():
    while True:
        print("Please enter cards as comma seperated indexes, eg: 0,1 or 4,5,6")
        move = input("Enter Pair or Trio of cards: ")

        try:
            move = [int(i) for i in move.replace(" ", "").split(",")]

            if len(move) not in [2, 3]:
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


def draw_card(filepath, x, y):
    imp = pygame.image.load(filepath).convert()
    imp = pygame.transform.scale(imp, (CARD_WIDTH, CARD_HEIGHT))
    screen.blit(imp, (x, y))
    pygame.draw.rect(screen, (0, 0, 0), (x, y, CARD_WIDTH, CARD_HEIGHT), 1)


def draw_cards(cards):
    for idx, card in enumerate(cards):
        filepath = card.get_image_filepath()

        rowNum = idx // 5
        colNum = idx % 5  # column in the row (0-4)

        x = colNum * (CARD_WIDTH + 20) + 10
        y = rowNum * (CARD_HEIGHT + 20) + 10

        draw_card(filepath, x, y)


def get_card_index_from_click(x, y, total_cards=9):
    cards_per_row = 5
    card_width = 100
    card_height = 146
    spacing = 20
    padding = 10

    x_adj = x - padding
    y_adj = y - padding

    if x_adj < 0 or y_adj < 0:
        return None

    # Calculate column and row based on card+spacing
    col = x_adj // (card_width + spacing)
    row = y_adj // (card_height + spacing)

    # Check if click is within the card area, not the spacing between cards
    within_x = x_adj % (card_width + spacing) < card_width
    within_y = y_adj % (card_height + spacing) < card_height

    if not (within_x and within_y):
        return None  # Click was in the gap between cards

    # Calculate index
    idx = int(row * cards_per_row + col)

    if idx >= total_cards:
        return None

    return idx


def highlight_card_by_index(index, colour):
    rowNum = index // 5
    colNum = index % 5

    x = colNum * (CARD_WIDTH + 20) + 10
    y = rowNum * (CARD_HEIGHT + 20) + 10

    pygame.draw.rect(screen, colour, (x, y, CARD_WIDTH, CARD_HEIGHT), 5)


while (
    tableCards.size() < 8 or getPossibleMoves(tableCards.cards) == []
) and gameDeck.size() > 0:
    tableCards.add_card(gameDeck.draw_card())

hint = False
playing = True
endTimeRecorded = False
startTime = time.time()

GUIoption = input("Would you like to play the game with the GUI (1) or CLI (2)?")

if GUIoption == "1":

    pygame.init()
    X = 600
    Y = 600

    screen = pygame.display.set_mode((X, Y))

    # set the pygame window name
    pygame.display.set_caption("image")
    font = pygame.font.SysFont(None, 60)
    fontsmall = pygame.font.SysFont(None, 30)

    while status:
        screen.fill((255, 255, 255))  # Clear screen

        for event in pygame.event.get():
            # Check if the 'h' key is pressed, if so show hint
            keys = pygame.key.get_pressed()
            if keys[pygame.K_h]:
                hint = True
            else:
                hint = False

            # Toggle card selection on click
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mouse_x, mouse_y = event.pos
                clicked_index = get_card_index_from_click(
                    mouse_x, mouse_y, total_cards=tableCards.size()
                )
                if clicked_index is not None:

                    # If selected then unselect it, if not selected then select it
                    if clicked_index in selected:
                        selected.remove(clicked_index)
                    else:
                        selected.append(clicked_index)

                        # If a valid move is selected
                        move = sorted(selected)
                        if move in getPossibleMoves(tableCards.cards):
                            tableCards.cards = [
                                card
                                for idx, card in enumerate(tableCards.cards)
                                if idx not in move
                            ]

                            if tableCards.size() == 0 and gameDeck.size() == 0:
                                playing = False

                            else:
                                # Redraw cards back into hand
                                while (
                                    tableCards.size() < 8
                                    or getPossibleMoves(tableCards.cards) == []
                                ) and gameDeck.size() > 0:
                                    tableCards.add_card(gameDeck.draw_card())

                            selected = []

            if event.type == pygame.QUIT:
                status = False

        if playing == True:
            draw_cards(tableCards.cards)

            for index in selected:
                highlight_card_by_index(index, (0, 0, 255))

            if hint:
                for index in getPossibleMoves(tableCards.cards)[0]:
                    highlight_card_by_index(index, (255, 100, 100))

            time_taken = time.time() - startTime
            time_text = fontsmall.render(f"Time: {time_taken:.2f} seconds", True, (0, 0, 0))
            screen.blit(time_text, (10, 575))

        else:
            if endTimeRecorded == False:
                time_taken = time.time() - startTime
                endTimeRecorded = True

            win_text = font.render("YOU WIN!", True, (0, 0, 0))
            time_text = font.render(f"Time: {time_taken:.2f} seconds", True, (0, 0, 0))

            screen.blit(win_text, (200, 150))
            screen.blit(time_text, (120, 230))

        pygame.display.flip()

    pygame.quit()

if GUIoption:
    startTime = time.time()
    playing = True
    while playing:
        # Debug: Display possible moves
    
        # Check for win or loss
        if tableCards.cards == []:
            print("You Win!")
            print(f"Time: {time.time() - startTime:.2f} seconds")
            playing = False
            break

        # Display cards on the table
        for i, card in enumerate(tableCards.cards):
            print(i, ": ", card.get_card_name())

        move = getUserInput()

        # Remove selected cards
        tableCards.cards = [card for idx, card in enumerate(tableCards.cards) if idx not in move]

        while (
            tableCards.size() < 8 or getPossibleMoves(tableCards.cards) == []
        ) and gameDeck.size() > 0:
            tableCards.add_card(gameDeck.draw_card())

else:
    print("Invalid option")