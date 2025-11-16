from cards import Deck, Card

testDeck = Deck()

for card in testDeck.get_cards():
    print("name: ", card.get_card_name(), " value: ", card.get_value())
