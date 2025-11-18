from cards import Deck, Card
from shuffler import Shuffler

testDeck = Deck()

testDeck.cards = Shuffler.casino_style_shuffle(testDeck.cards)

for card in testDeck.get_cards():
    print("name: ", card.get_card_name(), " value: ", card.get_value())
